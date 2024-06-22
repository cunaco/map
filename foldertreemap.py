import os

def generate_tree(start_path, indent=''):
    """
    Generate and print the directory tree starting at start_path.
    """
    # Ensure start_path is a valid directory
    if not os.path.isdir(start_path):
        print(f"Error: {start_path} is not a valid directory.")
        return
    
    # Get the contents of the directory
    contents = os.listdir(start_path)
    
    # Iterate over each item in the directory
    for i, item in enumerate(contents):
        # Construct full path
        full_path = os.path.join(start_path, item)
        
        # Determine prefix based on position in contents
        if i == len(contents) - 1:
            prefix = '└── '
        else:
            prefix = '├── '
        
        # Print the current item prefixed with indent
        print(indent + prefix + item)
        
        # Recursively descend into directories
        if os.path.isdir(full_path):
            if i == len(contents) - 1:
                generate_tree(full_path, indent + '    ')
            else:
                generate_tree(full_path, indent + '│   ')

# Example usage:
if __name__ == '__main__':
    path = input("Enter the directory path to generate tree map: ").strip()
    generate_tree(path)
