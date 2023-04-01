import React, { useState, useEffect } from 'react'
import { io } from "socket.io-client";

const Settings = ({ selectedRoom }) => {
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    const newSocket = io('http://localhost:5001');
    setSocket(newSocket);

    return () => {
      newSocket.disconnect();
    };
  }, []);

  const clearChat = () => {
    socket.emit("clear_room", selectedRoom);
  };

  return (
    <div className='bg-bgblack text-white border-l-[1px] border-white border-opacity-25 w-2/12'>
      <div className='p-6'>
        <p>Settings</p>
        <p> {selectedRoom} </p>

        <button className="text-xs border border-bglight rounded p-2 mt-2 hover:text-olive" onClick={clearChat}>Clear chat</button>
      </div>
      </div>
  )
}

export default Settings