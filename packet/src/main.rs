use std::net::{SocketAddr, IpAddr, Ipv4Addr};
use std::net::UdpSocket;

// flag{..} xored with 0xcc
static FLAG: &'static [u8] = &[170,160,173,171,183,191,188,163,163,170,147,184,164,169,147,161,173,171,165,175,147,168,190,173,171,163,162,177];

fn main() -> std::io::Result<()> {
    {
        let socket = UdpSocket::bind("0.0.0.0:34254")?;
        println!("안녕하세요!");

        // Receives a single datagram message on the socket. If `buf` is too small to hold
        // the message, it will be cut off.
        let mut buf = [0; 10];
        let (amt, src) = socket.recv_from(&mut buf)?;

        check_packet_port(&src);
        check_packet_ip(&src);
        // Redeclare `buf` as slice of the received data and send reverse data back to origin.
        let mut out = [0xcc; 28];
        for i in 0..28 {
            out[i] = out[i] ^ FLAG[i];
        }
        socket.send_to(&out, &src)?;
    } // the socket is closed here
    Ok(())
}

fn check_packet_port(src: &SocketAddr) {
    if src.port() != 1 {
        panic!("당신을 위해 깃발이 없습니다");
    }
}

fn check_packet_ip(src: &SocketAddr) {
    if src.ip() != IpAddr::V4(Ipv4Addr::new(175, 45, 179, 1)) {
        panic!("당신을 위해 깃발이 없습니다!");
    }
}
