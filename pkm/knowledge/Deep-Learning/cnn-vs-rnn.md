---
title: "cnn-vs-rnn"
status: draft
created: 2026-08-08
tags:
  - deep-learning
  - neural-networks
  - architectures
related:
  - neural-networks-basics
---

# cnn-vs-rnn

## Purpose

Compare convolutional networks and recurrent networks and the data each is
built for.

## Context

Different data has different structure, and a plain dense network ignores it.
Convolutional networks (CNNs) exploit the grid structure of images; recurrent
networks (RNNs) exploit the sequence structure of text and time series. Each
architecture builds structure into the network instead of learning it
from scratch.

## Main Notes

- A CNN slides small filters over an image, detecting local patterns like
  edges and textures.
- Convolutions share weights across the image, so a filter finds the same
  feature anywhere.
- Pooling shrinks the feature maps, building translation invariance and
  reducing computation.
- CNNs excel at images and any grid-structured data, such as audio
  spectrograms.
- An RNN processes a sequence one step at a time, carrying a hidden state
  that remembers context.
- RNNs learn from order: earlier inputs influence later outputs through the
  hidden state.
- RNNs suffer from vanishing gradients on long sequences; LSTM and GRU
  variants mitigate this.
- For text, transformers have largely replaced RNNs, while CNNs remain the
  basis of vision models.

## References

- Foundational concept; no single source.
- Standard deep learning textbook topic; CNNs from LeCun and RNNs from
  early sequential learning work.

## Related Notes

- [[neural-networks-basics]]

## Tags

This note is tagged in the front matter as deep-learning, neural-networks,
architectures.

## Review History

- 2026-08-08: Created as a draft.
