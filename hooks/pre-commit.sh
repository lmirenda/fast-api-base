#!/bin/bash
echo "Format code"
  isort . && black .
exit 0