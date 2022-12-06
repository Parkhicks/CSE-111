def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")

    fruit_list = fruit_list[::-1]
    print(f"reversed: {fruit_list}")

    fruit_list.append("orange")
    print(f"append orange: {fruit_list}")

    spot = fruit_list.index("apple")
    fruit_list.insert(spot,"cherry")
    print(f"insert cherry: {fruit_list}")

    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")

    element = fruit_list.pop()
    print(f"pop {element}: {fruit_list}")

    fruit_list.sort()
    print(f"sorted: {fruit_list}")

    fruit_list = []
    print(f"cleared: {fruit_list}")


main()