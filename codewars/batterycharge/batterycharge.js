function calculateTime(battery,charger){
   
    let num = ((battery * 0.85) / charger) + ((battery * 0.10) / (charger * 0.50)) + ((battery * 0.05) / (charger * 0.20));
    return Math.round(num * 100) / 100; // hack needed for rounding
      
  }
  