export type ImageMeta = {
    box_contours?:        Array<Array<Array<number[]>>> | null;
    grid_coords?:         null | Rectangle;
    perspective_corners?: any[] | null;
    source?:              Source | null;
    [property: string]: any;
}


export type Source = "raw-scan" | "corrected-scan" | "camera" | "corrected-camera" | "robust-corrected";

  // hand-generated since quicktype treats `[number, number]` as `any[]`
  export type Rectangle = {
    size: [number, number]
    tl: [number, number]
  }
  