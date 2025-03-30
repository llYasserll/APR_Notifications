import { Connection, ConnectionConfig, Commitment, Keypair } from "@solana/web3.js";
import bs58 from "bs58"

//FROM SECRETEKEY
const connection = new Connection("https://api.devnet.solana.com")
const secretkey = bs58.decode("tu clave privada aqui")
const restoredKeypair = Keypair.fromSecretKey(secretkey)

console.log("Restored Public Key:", restoredKeypair.publicKey.toBase58());

async function getBalance() {
    try {
        const balance = await connection.getBalance(restoredKeypair.publicKey);
        console.log(`Balance: ${balance / 1e9} SOL`); // Convertir lamports a SOL
    } catch (error) {
        console.error("Error al obtener el balance:", error);
    }
}

getBalance();