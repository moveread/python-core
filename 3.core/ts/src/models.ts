export type Game = {
    id:      string;
    meta?:   GameMeta | null;
    players: Player[];
}

export type GameMeta = {
    early?:      boolean | null;
    headers?:    Headers | null;
    pgn?:        string[] | null;
    tournament?: Tournament | null;
}

export type Headers = {
    black?:  null | string;
    date?:   null | string;
    event?:  null | string;
    result?: null | string;
    round?:  number | null;
    site?:   null | string;
    white?:  null | string;
}

export type Tournament = {
    board?: number | null;
    group?: null | string;
    name?:  null | string;
    round?: number | null;
}

export type Player = {
    meta?:  null | PlayerMeta;
    sheets: Sheet[];
}

export type PlayerMeta = {
    end_correct?:   number | null;
    language?:      Language | null;
    manual_labels?: { [key: string]: string } | null;
    styles?:        null | StylesNA;
    [property: string]: any;
}

export type Language = "CA" | "EN" | "DE" | "RU" | "RO" | "BG" | "FR" | "AZ" | "TR" | "PL" | "IS" | "NL" | "DK" | "N/A";

/**
 * Like `chess_notation.Styles`, but with possibly `'N/A'` annotations
 */
export type StylesNA = {
    castle?:        Castle | null;
    check?:         Check | null;
    mate?:          Mate | null;
    pawn_capture?:  PawnCapture | null;
    piece_capture?: PieceCapture | null;
    [property: string]: any;
}

export type Castle = "OO" | "O-O" | "N/A";

export type Check = "NONE" | "CHECK" | "N/A";

export type Mate = "NONE" | "SHARP" | "DOUBLE_CHECK" | "N/A";

export type PawnCapture = "de" | "dxe" | "de4" | "dxe4" | "xe4" | "PxN" | "N/A";

export type PieceCapture = "Ne4" | "Nxe4" | "NxN" | "N/A";

export type Sheet = {
    images: Image[];
    meta?:  null | SheetMeta;
}

export type Image = {
    boxes?: Box[] | null;
    meta?:  null | ImageMeta;
    url:    string;
}

export type Box = {
    meta?: { [key: string]: any } | null;
    url:   string;
}

export type ImageMeta = {
    box_contours?:        Array<Array<Array<number[]>>> | null;
    grid_coords?:         null | Rectangle;
    perspective_corners?: any[] | null;
    source?:              Source | null;
    [property: string]: any;
}

export type Rectangle = {
    size: any[];
    tl:   any[];
    [property: string]: any;
}

export type Source = "raw-scan" | "corrected-scan" | "camera" | "corrected-camera" | "robust-corrected";

export type SheetMeta = {
    model?: Model | null;
    [property: string]: any;
}

export type Model = "fcde" | "llobregat23";
