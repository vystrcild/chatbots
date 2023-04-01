import React, { useState, useEffect } from 'react';
import { io } from 'socket.io-client';

const Settings = ({ selectedRoom }) => {
  const [socket, setSocket] = useState(null);
  const [model, setModel] = useState('gpt-3.5-turbo');
  const [room_name, setRoomName] = useState(selectedRoom);

  useEffect(() => {
    const newSocket = io('http://localhost:5001');
    setSocket(newSocket);

    return () => {
      newSocket.disconnect();
    };
  }, []);

  useEffect(() => {
    setRoomName(selectedRoom);
  }, [selectedRoom]);

  const clearChat = () => {
    socket.emit('clear_room', selectedRoom);
  };

  const handleModelChange = (e) => {
    setModel(e.target.value);
  };

  const handleRoomNameChange = (e) => {
    setRoomName(e.target.value);
  };

  const saveSettings = () => {
    socket.emit('settings', { room_name, model });
  };

  return (
    <div className="bg-bgblack text-white border-l-[1px] border-white border-opacity-25 w-2/12">
      <div className="p-6 flex flex-col">
        <p>Settings</p>
        <input
          type="text"
          value={room_name}
          onChange={handleRoomNameChange}
          className="bg-bgblack text-sm my-2"
        />

        <select
          value={model}
          onChange={handleModelChange}
          className="bg-bgblack text-sm my-2"
        >
          <option value="gpt-3.5-turbo">gpt-3.5-turbo</option>
          <option value="gpt-4">gpt-4</option>
        </select>

        <button
          className="text-xs border border-bglight rounded p-2 mt-2 hover:text-olive"
          onClick={saveSettings}
        >
          Save
        </button>
        <br />
        <button
          className="mt-auto text-xs border border-bglight rounded p-2 hover:text-olive"
          onClick={clearChat}
        >
          Clear {selectedRoom}
        </button>
      </div>
    </div>
  );
};

export default Settings;
