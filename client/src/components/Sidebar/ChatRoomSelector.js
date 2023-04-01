import React from 'react';

const rooms = [
  { id: 'farnam', name: 'Farnam Street' },
  { id: 'chat_test', name: 'OpenAI chat' },
  { id: 'room2', name: 'Chat Room 2' },
  { id: 'room3', name: 'Chat Room 3' },
];

const ChatRoomSelector = ({ selectedRoom, onSelectRoom }) => {
  const handleRoomSelect = (e) => {
    e.preventDefault();
    const roomId = e.target.dataset.roomId;
    onSelectRoom(roomId);
  };

  return (
    <div>
      <ul className="mt-4">
        {rooms.map((room) => (
          <li key={room.id}>
            <div className='p-2 m-2 rounded-md border border-bglight text-xs'>
            <a
              className={`${
                room.id === selectedRoom ? 'text-primary' : 'text-white'
              } hover:text-olive`}
              href="#"
              onClick={handleRoomSelect}
              data-room-id={room.id}
            >
              {room.name}
            </a>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ChatRoomSelector;
