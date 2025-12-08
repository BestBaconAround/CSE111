def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")
  fruit_list.reverse()
  print(fruit_list)
  fruit_list.append("orange")

  location = fruit_list.index("apple")
  print(location)
  fruit_list.insert(1, "cherry")
  fruit_list.remove("banana")

  fruit_popped = fruit_list.pop()
  print(fruit_popped)
  fruit_list.sort()
  print(f"fruit sorted: {fruit_list}")
  fruit_list.clear()
  print(f"list cleared {fruit_list}")
  print(fruit_list)
main()
