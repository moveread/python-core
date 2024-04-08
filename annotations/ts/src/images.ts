export type ImageMeta = {
    box_contours?:      Array<Array<Array<number[]>>> | null;
    grid_coords?:       null | Rectangle;
    robust_extraction?: RobustExtraction | null;
    source?:            Source | null;
    [property: string]: any;
}


export type RobustExtraction = "failed" | "incorrect" | "perspective-correct" | "correct";

export type Source = "raw-scan" | "corrected-scan" | "camera" | "corrected-camera" | "robust-corrected";

  // hand-generated as quicktype treats `[number, number]` as `any[]`
  export type Rectangle = {
    size: [number, number]
    tl: [number, number]
  }
  