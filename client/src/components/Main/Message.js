import React from 'react'
import getAvatarUrl from '../../helpers/avatarHelper';

const Message = ({ user, text, datetime }) => {
  const messageClass = user === "Me" ? "text-olive" : "text-primary";
  const avatarUrl = getAvatarUrl(user);
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    const now = new Date();
    const yesterday = new Date(now);
    yesterday.setDate(now.getDate() - 1);

    const isToday = date.toDateString() === now.toDateString();
    const isYesterday = date.toDateString() === yesterday.toDateString();

    const timeFormatOptions = { hour: '2-digit', minute: '2-digit', hour12: false };
    const timeFormatted = new Intl.DateTimeFormat('en-US', timeFormatOptions).format(date);

    if (isToday) {
      return timeFormatted;
    }

    if (isYesterday) {
      return `Yesterday ${timeFormatted}`;
    }

    const dateFormatOptions = date.getFullYear() === now.getFullYear() ? { month: '2-digit', day: '2-digit' } : { year: 'numeric', month: '2-digit', day: '2-digit' };
    const dateFormat = new Intl.DateTimeFormat('en-US', dateFormatOptions).format(date);

    return `${dateFormat} ${timeFormatted}`;
  };

  const formattedDatetime = formatDate(datetime);

  return (
    <div className="flex text-white py-8 px-4 w-full justify-center">
      <div className='w-6/12 flex justify-center'>
      <img src={avatarUrl} alt={`${user} avatar`} className="w-10 h-10 rounded-full mr-4 mt-1" />

      <div className='flex flex-col space-y-2 w-full'>
      <div className="flex flex-row items-baseline justify-between">
        <p className={`font-medium text-sm ${messageClass}`}>{user}</p>
        <p className="text-xs text-bglight">{formattedDatetime}</p>
      </div>
      <p className="text-xs text-justify whitespace-pre-wrap">{text}</p>
    </div>
    </div>
    </div>
  )
}

export default Message
