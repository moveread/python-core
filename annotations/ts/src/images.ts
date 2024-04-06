export type ImageMeta = {
    grid_coords?: null | Rectangle;
    source?:      Source | null;
}


export type Source = "raw-scan" | "corrected-scan" | "camera" | "corrected-camera";

  // hand-generated as quicktype treats `[number, number]` as `any[]`
  export type Rectangle = {
    size: [number, number]
    tl: [number, number]
  }
  