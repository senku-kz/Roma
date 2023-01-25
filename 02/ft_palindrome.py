if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
    else:
        s = sys.argv[1]
        if s == s[::-1]:
            print("Yes")
        else:
            print("No")
