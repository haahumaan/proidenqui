import numpy as np

def spherical_to_cartesian(lat, lon):
    """Convert spherical coordinates to Cartesian coordinates."""
    lat_rad = np.radians(lat)
    lon_rad = np.radians(lon)
    x = np.cos(lat_rad) * np.cos(lon_rad)
    y = np.cos(lat_rad) * np.sin(lon_rad)
    z = np.sin(lat_rad)
    return np.array([x, y, z])

def great_circle_intersects_clip_circle(A, B, clip_center, clip_radius):
    """Check if the great circle defined by points A and B intersects the clip circle."""
    # Convert points to Cartesian coordinates
    A_cart = spherical_to_cartesian(A[0], A[1])
    B_cart = spherical_to_cartesian(B[0], B[1])
    clip_center_cart = spherical_to_cartesian(clip_center[0], clip_center[1])
    
    # Normal vector to the plane of the great circle
    normal_vector = np.cross(A_cart, B_cart)
    
    # Find intersection points of the plane with the sphere
    # The equation of the plane is normal_vector . X = 0
    # We solve (normal_vector . X)^2 = 1
    a = normal_vector[0]**2 + normal_vector[1]**2 + normal_vector[2]**2
    b = 2 * (normal_vector[0] * clip_center_cart[0] +
             normal_vector[1] * clip_center_cart[1] +
             normal_vector[2] * clip_center_cart[2])
    c = clip_center_cart[0]**2 + clip_center_cart[1]**2 + clip_center_cart[2]**2 - 1
    
    # Solve quadratic equation for t
    delta = b**2 - 4*a*c
    if delta < 0:
        return False  # No intersection
    
    t1 = (-b + np.sqrt(delta)) / (2*a)
    t2 = (-b - np.sqrt(delta)) / (2*a)
    
    # Calculate intersection points
    intersection1 = t1 * normal_vector
    intersection2 = t2 * normal_vector
    
    # Check if intersections are within the clip circle
    dist1 = np.linalg.norm(intersection1 - clip_center_cart)
    dist2 = np.linalg.norm(intersection2 - clip_center_cart)
    
    return dist1 <= clip_radius or dist2 <= clip_radius

# Example usage
A = (lat1, lon1)  # Point A in (latitude, longitude)
B = (lat2, lon2)  # Point B in (latitude, longitude)
clip_center = (clip_lat, clip_lon)  # Center of the clipping circle
clip_radius = clip_radius_value  # Radius of the clipping circle

intersects = great_circle_intersects_clip_circle(A, B, clip_center, clip_radius)
print("Intersects:", intersects)
