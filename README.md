# My Study Log

This repository records my learning and small implementations around parser, AST, evaluator, and basic optimization passes.

## Overview

The current focus is on understanding how structured program representations are built and transformed through small examples.

So far, this repository includes:

- tokenizer / lexical analysis
- parser / syntax analysis
- precedence-aware expression parsing
- AST construction
- evaluator
- very small constant folding

## Repository Structure

- `week1/`
  - basic environment and coding practice
  - tokenizer / parser / AST related early steps
- `week2/`
  - precedence parser
  - evaluator
  - constant folding
  - concept notes on compiler pipeline

## Highlights

Representative examples in this repository include:

- expression tokenizer
- precedence parser with `+ - * /` and parentheses
- AST-based evaluator
- very small constant folding pass on AST

## Current Goal

The goal of this repository is to build a clearer understanding of:

- program representation
- parsing
- AST-based processing
- simple tree transformation and optimization ideas

## Example

A typical workflow in the current code is:

1. tokenize input text into tokens
2. parse tokens into an AST
3. run a very small constant folding pass
4. evaluate the folded AST

## Notes

This is a learning-oriented repository.  
The implementations are intentionally small and focused on understanding core ideas step by step.