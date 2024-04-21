export type PlayerMeta = {
    end_correct?:   number | null;
    language?:      Language | null;
    manual_labels?: { [key: string]: string } | null;
    styles?:        null | Styles;
}

export type Language = "CA" | "EN" | "DE" | "RU" | "RO" | "BG" | "FR" | "AZ" | "TR" | "PL" | "IS" | "NL" | "DK";

export type Styles = {
    castle?:        Castle | null;
    check?:         Check | null;
    mate?:          Mate | null;
    pawn_capture?:  PawnCapture | null;
    piece_capture?: PieceCapture | null;
    [property: string]: any;
}

export type Castle = "OO" | "O-O";

export type Check = "NONE" | "CHECK";

export type Mate = "NONE" | "SHARP" | "DOUBLE_CHECK";

export type PawnCapture = "de" | "dxe" | "de4" | "dxe4" | "xe4" | "PxN";

export type PieceCapture = "Ne4" | "Nxe4" | "NxN";
