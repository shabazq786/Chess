import socketIOClient from "socket.io-client";
const ENDPOINT = "https://chess-287107.wl.r.appspot.com/";
export var socket = socketIOClient(ENDPOINT);



