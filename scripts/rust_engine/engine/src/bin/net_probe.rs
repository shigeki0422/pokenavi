use serde_json::Value;
fn main(){
    let a: Vec<String> = std::env::args().collect();
    let v: Value = serde_json::from_str(&std::fs::read_to_string(&a[1]).unwrap()).unwrap();
    let x: Vec<f64> = v["x"].as_array().unwrap().iter().map(|z|z.as_f64().unwrap()).collect();
    let w: Vec<f64> = v["w"].as_array().unwrap().iter().map(|z|z.as_f64().unwrap()).collect();
    let mut hx=0u64; for z in &x { hx = hx.wrapping_mul(1000003).wrapping_add(z.to_bits()); }
    let mut hw=0u64; for z in &w { hw = hw.wrapping_mul(1000003).wrapping_add(z.to_bits()); }
    println!("hx={:x} hw={:x}", hx, hw);
    let mut acc=0.0f64;
    for k in 0..x.len(){ acc+=x[k]*w[k]; if k%100==0 {println!("k={} {:x}",k,acc.to_bits());} }
}
