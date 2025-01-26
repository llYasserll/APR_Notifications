import { SuiClient, getFullnodeUrl } from '@mysten/sui/client';
import { Ed25519Keypair } from '@mysten/sui/keypairs/ed25519';
import { decodeSuiPrivateKey } from '@mysten/sui/cryptography';
import dotenv from "dotenv"
import path = require('path');

dotenv.config({ path: path.dirname(__dirname) + '/.env' });
async function getWalletBalance(privateKey: string, env: 'mainnet') {
    const keypair = Ed25519Keypair.fromSecretKey(decodeSuiPrivateKey(privateKey).secretKey);
    const suiClient = new SuiClient({ url: getFullnodeUrl(env) });
    const address = keypair.toSuiAddress();
  
    
    const balanceParams = { owner: address };
    const balance = await suiClient.getBalance(balanceParams);
    console.log('Balance:', balance);
  }
  dotenv.config();
  const privateKey = process.env.privatekey || '';
  getWalletBalance(privateKey, 'mainnet').catch(console.error);
