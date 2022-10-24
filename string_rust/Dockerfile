FROM rust:latest
COPY . ./string_rust
WORKDIR /string_rust
RUN cargo build --release
EXPOSE 5000
CMD ["./target/release/string_rust"]