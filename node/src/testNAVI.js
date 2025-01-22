"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const dotenv_1 = __importDefault(require("dotenv"));
const navi_sdk_1 = require("navi-sdk");
dotenv_1.default.config();
const mnemonic = process.env.mnemonic;
const rpc = "https://fullnode.mainnet.sui.io:443";
// Use an existing mnemonic or leave empty to generate a new one
const client = new navi_sdk_1.NAVISDKClient({
    mnemonic,
    networkType: rpc,
    numberOfAccounts: 1
});
const account = client.account;
const address = account.address;
account.getPublicKey();
console.log(address);
