function spaceJam(s) {

  let removed_space = s.replace(/\s+/g, "");
  let spacejam_s = removed_space.split('').join('  ').toUpperCase();
  
  return spacejam_s;
}

// Test Stage
console.log(spaceJam("hello world")); 