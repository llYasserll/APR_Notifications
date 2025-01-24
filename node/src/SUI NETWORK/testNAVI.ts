import dotenv from "dotenv"
import { NAVISDKClient } from "navi-sdk";

dotenv.config();

const mnemonic = process.env.mnemonic; 
const rpc = "https://fullnode.mainnet.sui.io:443";
// Use an existing mnemonic or leave empty to generate a new one
const client = new NAVISDKClient({
  mnemonic,
  networkType: rpc, 
  numberOfAccounts: 1
}); 
const account = client.account;

const address = account.address;
account.getPublicKey();
console.log(address);
