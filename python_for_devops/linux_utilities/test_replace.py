def needs_root():
    """Check if this action requires superuser privileges."""
    return True

# Example usage
if needs_root:
    print("Root required")
