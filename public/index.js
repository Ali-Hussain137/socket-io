const sio = io();

sio.on("connect", () => {
  console.log("Connected");
  sio.emit("sum", { number: [1, 2] }, (result) => {
    console.log(result);
  });
});

sio.on("disconnect", () => {
  console.log("Disconnected");
});

sio.on("sum_result", (data) => {
  console.log(data);
});

sio.on("mult", (data, cb) => {
  result = data.numbers[0] * data.numbers[1];
  cb(result);
});

sio.on("client_count", (clientCount) => {
  console.log("There are " + clientCount + " client connected");
});

sio.on("room_count", (count) => {
  console.log("There are " + count + " clients  connected in this room");
});

sio.on("user_joined", (username) => {
  console.log(`Joined ${username}`);
});

sio.on("user_left", (username) => {
  console.log(`left ${username}`);
});
