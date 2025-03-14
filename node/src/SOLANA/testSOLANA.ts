import { Connection, ConnectionConfig, Commitment, Keypair } from "@solana/web3.js";
import bs58 from "bs58"

//FROM SECRETEKEY
const connection = new Connection("https://api.devnet.solana.com")
const secretkey = bs58.decode("tu clave privada aqui")
const restoredKeypair = Keypair.fromSecretKey(secretkey)

console.log("Restored Public Key:", restoredKeypair.publicKey.toBase58());