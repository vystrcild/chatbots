
const getAvatarUrl = (user) => {
  if (user === "Me") {
    return "/assets/images/me_avatar.png"; // Replace with your image filename
  } else if (user === "Farnam Street") {
    return "/assets/images/farnam.png"; // Replace with your image filename
  } else {
    // Add more cases for other channels, or return a default avatar
    return "/assets/images/avatar.png"; // Replace with your image filename
  }
};

export default getAvatarUrl;
