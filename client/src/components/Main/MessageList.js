import React, { useEffect, useRef } from 'react'
import Message from './Message';
import { LineWave } from 'react-loader-spinner';


const MessageList = ({ messages, isLoading }) => {
  const messageListRef = useRef(null);

  useEffect(() => {
    if (messageListRef.current) {
      messageListRef.current.scrollTop = messageListRef.current.scrollHeight;
    }
  }, [messages]);

  return (


    <div className="flex-1 overflow-y-auto bg-bgblack" ref={messageListRef}>
        {messages.map((message) => (
        <Message
          key={message.id}
          user={message.user}
          text={message.text}
          datetime={message.datetime}
        />
      ))}
      {isLoading && (
        <div className="flex items-center justify-center p-4">
          <LineWave color="#45ffbc" height="50" width="50" />
        </div>
      )}
    </div>

  )
}

export default MessageList