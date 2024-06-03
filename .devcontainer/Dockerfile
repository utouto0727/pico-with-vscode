# Use the official Python base image
FROM ubuntu:22.04

# Install required dependencies
RUN apt-get update && apt-get install -y \
    git \
    locales

# 日本語が使えるようにする
RUN locale-gen ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
