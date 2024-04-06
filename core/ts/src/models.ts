export type Game = {
    id:      string;
    meta?:   { [key: string]: any } | null;
    players: Player[];
}

export type Player = {
    meta?:  { [key: string]: any } | null;
    sheets: Sheet[];
}

export type Sheet = {
    images: Image[];
    meta?:  { [key: string]: any } | null;
}

export type Image = {
    boxes?: Box[] | null;
    meta?:  { [key: string]: any } | null;
    url:    string;
}

export type Box = {
    meta?: { [key: string]: any } | null;
    url:   string;
}
