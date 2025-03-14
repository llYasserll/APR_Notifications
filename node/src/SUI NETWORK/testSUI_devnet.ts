import { getFullnodeUrl, SuiClient } from '@mysten/sui/client';
import { SerialTransactionExecutor, Transaction } from '@mysten/sui/transactions';
import { Ed25519Keypair } from '@mysten/sui/keypairs/ed25519';
import dotenv from 'dotenv'
import path from 'path'
 
// get coins owned by an address
// replace <OWNER_ADDRESS> with actual address in the form of 0x123...
/*async function GetCoins() {
    const coins = await client.getCoins({
        owner: '0xedecc40ac98caa1aca045a7bec7de92a8fc851de1979c1ca9558349b1c29a1c1',
    });
    console.log(coins)
}
GetCoins();*/


// Cargar las variables de entorno
dotenv.config({ path: path.dirname(__dirname) + '/.env' });
const mnemonic = process.env.mnemonic || '';
// Definir el cliente y el mnemonic
const client = new SuiClient({ url: getFullnodeUrl('devnet') });
const keypair = Ed25519Keypair.deriveKeypair(mnemonic);

//console.log(keypair)

 
const executor = new SerialTransactionExecutor({
	client,
	signer: keypair,
});

const tx1 = new Transaction();
const [coin1] = tx1.splitCoins(tx1.gas, [1000000000]);
tx1.transferObjects([coin1], '0xec3b7674b92a886053dbb390aaac758ce2fbb485a37040b3d2f611912e7f24b7');


(async () => {
    const [{ digest: digest1 }] = await Promise.all([
        executor.executeTransaction(tx1)
    ]);
    console.log('Digest:', digest1);
})();











