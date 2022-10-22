FROM rust:latest
COPY . ./string_rust
WORKDIR /string_rust
RUN cargo build --release
CMD ["./target/release/string_rust"]