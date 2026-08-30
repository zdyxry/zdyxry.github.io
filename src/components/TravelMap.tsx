import { useEffect, useRef } from 'react';
import maplibregl from 'maplibre-gl';
import 'maplibre-gl/dist/maplibre-gl.css';

interface TravelPlace {
  id: string;
  name: string;
  nameEn: string;
  coordinates: [number, number];
  date: string;
  type: 'domestic' | 'international' | 'work' | 'leisure';
  description?: string;
  photos?: string[];
}

interface Props {
  places: TravelPlace[];
}

const typeLabels: Record<TravelPlace['type'], string> = {
  domestic: '国内',
  international: '出境',
  work: '出差',
  leisure: '休闲',
};

const typeColors: Record<TravelPlace['type'], string> = {
  domestic: '#2563eb',
  international: '#7c3aed',
  work: '#059669',
  leisure: '#ea580c',
};

export default function TravelMap({ places }: Props) {
  const mapContainer = useRef<HTMLDivElement>(null);
  const mapRef = useRef<maplibregl.Map | null>(null);
  const markersRef = useRef<maplibregl.Marker[]>([]);

  useEffect(() => {
    if (!mapContainer.current || mapRef.current) return;

    const map = new maplibregl.Map({
      container: mapContainer.current,
      style: 'https://tiles.openfreemap.org/styles/positron',
      center: [110, 35],
      zoom: 3,
      attributionControl: {
        compact: true,
        customAttribution:
          '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors',
      },
    });

    map.addControl(new maplibregl.NavigationControl(), 'top-right');
    map.addControl(new maplibregl.FullscreenControl(), 'top-right');

    map.on('load', () => {
      // Fit bounds to show all markers
      if (places.length > 0) {
        const bounds = new maplibregl.LngLatBounds();
        places.forEach((place) => bounds.extend(place.coordinates));
        map.fitBounds(bounds, { padding: 80, maxZoom: 10, duration: 1000 });
      }
    });

    mapRef.current = map;

    return () => {
      markersRef.current.forEach((marker) => marker.remove());
      markersRef.current = [];
      map.remove();
      mapRef.current = null;
    };
  }, []);

  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;

    // Clear existing markers
    markersRef.current.forEach((marker) => marker.remove());
    markersRef.current = [];

    places.forEach((place) => {
      const color = typeColors[place.type];
      const el = document.createElement('div');
      el.className = 'travel-marker';
      el.style.width = '8px';
      el.style.height = '8px';
      el.style.borderRadius = '50%';
      el.style.background = color;
      el.style.border = '1.5px solid var(--background, #fff)';
      el.style.boxShadow = '0 1px 4px rgba(0,0,0,0.25)';
      el.style.cursor = 'pointer';

      const popup = new maplibregl.Popup({ offset: 12, closeButton: false }).setHTML(
        `<div style="min-width:180px;max-width:260px;font-family:inherit;">
          <div style="font-weight:600;font-size:1rem;margin-bottom:4px;">${place.name}</div>
          <div style="font-size:0.75rem;color:var(--text-secondary,#64748b);margin-bottom:6px;">${place.nameEn} · ${place.date}</div>
          ${place.description ? `<div style="font-size:0.875rem;line-height:1.5;color:var(--text-primary,#0f172a);">${place.description}</div>` : ''}
          <div style="margin-top:8px;">
            <span style="display:inline-block;font-size:0.75rem;padding:2px 8px;border-radius:999px;background:${color}20;color:${color};border:1px solid ${color}40;">${typeLabels[place.type]}</span>
          </div>
        </div>`
      );

      const marker = new maplibregl.Marker({ element: el, anchor: 'center' })
        .setLngLat(place.coordinates)
        .setPopup(popup)
        .addTo(map);

      marker.getElement().addEventListener('click', () => {
        map.flyTo({ center: place.coordinates, zoom: 10, duration: 800 });
      });

      markersRef.current.push(marker);
    });
  }, [places]);

  return (
    <div className="travel-map-wrapper">
      <div ref={mapContainer} className="travel-map" />
    </div>
  );
}
