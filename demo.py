name: Dev env workflow

on:
  push:

jobs:
  Test:
    runs-on: ubuntu-latest
    steps: 
      - uses: actions/checkout@v3
      - run: echo "Tell it was automatically triggered by a ${{ github.event_name }} event."
      - run: python demo.py