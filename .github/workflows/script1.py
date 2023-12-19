import os

def main():
  print("Hello from GitHub Actions!")
  token = os.environ.get("DAN_SECRET_TOKEN")
  if not token:
    raise RuntimeError("DAN_SECRET_TOKEN env var is not set!")
  print("All good! I found my env var")

if __name__ == '__main__':
  main()
