function milePace(miles, duration) {
  const [minutes , seconds] = duration.split(":").map(Number);

  const totalSeconds = minutes * 60 + seconds;
    
  const avgSeconds = totalSeconds / miles;
  const avgMinutes = Math.floor(avgSeconds / 60);
  const avgSecondsRemainder = Math.floor(avgSeconds % 60);

   return `${avgMinutes.toString().padStart(2, '0')}:${avgSecondsRemainder.toString().padStart(2, '0')}`;
}