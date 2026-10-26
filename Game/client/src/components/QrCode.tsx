import { useEffect, useState } from "react";
import QRCode from "qrcode";

export function QrCode({ value, className }: { value: string; className?: string }) {
  const [src, setSrc] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    void QRCode.toDataURL(value, {
      margin: 1,
      width: 480,
      errorCorrectionLevel: "M",
      color: { dark: "#14120c", light: "#f4f0e6" },
    }).then((url) => {
      if (!cancelled) setSrc(url);
    });
    return () => {
      cancelled = true;
    };
  }, [value]);

  if (!src) return <div className={className ? `${className} qr-pending` : "qr-pending"} />;
  return <img className={className} src={src} alt={`QR code for ${value}`} />;
}
