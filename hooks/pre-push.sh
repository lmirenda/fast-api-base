#!/bin/bash
echo "Running flake8 and tests..."
  flake8 && pytest -x
  code=$?
  if [ "$code" -eq "0" ]; then
      echo
      echo
      echo "All tests passed :)."
      echo
  else
      echo
      echo
      echo "Please (re)check tests! :("
            exit 1
  fi;
exit 0