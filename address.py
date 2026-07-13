def resolve_address(address_str):
    try:
        parts = address_str.split('-')
        if len(parts) != 3:
            raise ValueError("Invalid format")
            
        x_coord = int(parts[1])
        y_coord = int(parts[2])
        return (x_coord, y_coord)
        
    except Exception:
        return None