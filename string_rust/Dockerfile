FROM rust:latest
WORKDIR /string_rust
COPY . .
EXPOSE 5000
RUN cargo install --path .
CMD ["string_rust"]