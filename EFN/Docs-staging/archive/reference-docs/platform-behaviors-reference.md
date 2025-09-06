# Platform Behaviors Reference - Fieldmark v3

> **⚠️ DEPRECATED**: This document has been superseded by the consolidated [Platform Reference](../../references/platform-reference.md). This archived version is maintained for reference only.

## Overview {essential}

This reference document consolidates platform-specific behaviors across all Fieldmark v3 field types. Understanding these platform differences is critical for successful deployment and user experience optimization.

## Platform Characteristics Summary {essential}

| Platform | Performance | UI Framework | Primary Constraints |
|----------|-------------|--------------|-------------------|
| iOS | Moderate | Native WebView | Memory limits, permission cascades |
| Android | Variable | Chrome WebView | Device fragmentation, background restrictions |
| Web Desktop | Fast | Browser native | Network latency, no offline |
| Web Mobile | Slow | Mobile browser | Limited memory, touch UI |

## iOS Specific Behaviors {important}

### System Characteristics
- **Rendering Engine**: WebKit/Safari
- **Memory Limit**: ~200MB before crash
- **JavaScript Execution**: Single-threaded with 10s timeout
- **Local Storage**: 50MB IndexedDB limit
- **Performance**: ~2x slower than native apps

### UI Behaviors
- **System Font**: San Francisco (affects text measurements)
- **Touch Targets**: Minimum 44px WCAG requirement (Fieldmark uses 36px)
- **Keyboard**: Automatic avoidance with viewport adjustment
- **Safe Area**: Automatic constraints for notch/home indicator
- **Picker Controls**: Always full-screen modal
- **Back Navigation**: Swipe gestures enabled

### Permission Handling
```
Permission Request Flow:
1. System prompt (one-time)
2. Settings → Privacy if denied
3. Cannot re-prompt programmatically
4. Must guide user to Settings app
```

#### Camera Permissions
- Prompt appears on first camera field interaction
- Combined photo library and camera access
- HEIC images automatically converted to JPG
- Memory spikes during image processing

#### Location Permissions
- Three levels: Never, While Using, Always
- "While Using" sufficient for all Fieldmark features
- Background GPS drains battery significantly
- Accuracy stabilization requires 30-60 seconds
- Altitude always returns 0 in simulator

### File Handling
- No direct file system access
- Photos through UIImagePicker only
- Downloads go to Files app
- Cannot access arbitrary paths
- Share sheet for exports

## Android Specific Behaviors {important}

### System Characteristics
- **Rendering Engine**: Chrome WebView (version varies)
- **Memory Management**: Aggressive background killing
- **Storage**: External storage with scoped access
- **Performance**: Highly device-dependent
- **API Variations**: Significant across Android versions

### UI Behaviors
- **System Fonts**: Roboto (may vary by manufacturer)
- **Touch Targets**: Material Design 48dp recommendation
- **Back Button**: Hardware/software handling required
- **Keyboard**: Behavior varies by manufacturer
- **Navigation**: Bottom bar interference possible
- **Orientation**: Manual handling required

### Permission Handling
```
Runtime Permission Model:
1. Request at feature use
2. Can re-request if denied
3. "Don't ask again" checkbox
4. Rationale UI recommended
```

#### Storage Permissions
- Storage Access Framework (Android 10+)
- Legacy external storage (Android 9-)
- MediaStore for images/videos
- Document provider for files
- Path vs URI confusion common

#### Location Permissions
- Fine vs Coarse location
- Background location separate permission
- Battery optimization interference
- GPS wake-up delays (5-10 seconds)
- Network location fallback

### File Handling
- File size limits vary by device
- URI vs file path issues
- MediaStore integration required
- Content resolver for access
- Temporary file cleanup needed

## Web Desktop Specific Behaviors {important}

### Browser Support Matrix
| Browser | Support Level | Known Issues |
|---------|--------------|--------------|
| Chrome | Full | None |
| Safari | Good | IndexedDB limits |
| Firefox | Good | Camera API differences |
| Edge | Full | Legacy mode issues |

### Capabilities
- **Drag and Drop**: Full support for file fields
- **Clipboard**: Full read/write access
- **File System**: Limited to downloads folder
- **Multi-window**: Supported with session sharing
- **DevTools**: Full debugging capabilities

### Performance
- No memory constraints (system-dependent)
- Faster processing than mobile
- Better network handling
- No battery considerations
- Multiple concurrent operations

### Limitations
- No native GPS (IP/WiFi geolocation only)
- No camera access without HTTPS
- Local storage varies by browser
- No offline without service worker
- Print formatting inconsistent

## Web Mobile Specific Behaviors {important}

### Characteristics
- Limited memory (similar to native apps)
- Touch-optimized UI required
- No app store distribution
- PWA capabilities available
- Viewport management critical

### Browser Variations
- Safari iOS: Most restrictive
- Chrome Android: Most capable
- Firefox Mobile: Limited usage
- Samsung Internet: Custom behaviors

### Limitations
- No background processing
- Limited file system access
- Reduced performance vs native
- No push notifications (iOS)
- Share API limited

## Cross-Platform Considerations {essential}

### Performance Scaling
```
Relative Performance (normalized to Web Desktop = 1.0):
- Web Desktop: 1.0x (baseline)
- iOS Native: 0.5x
- Android High-end: 0.6x
- Android Mid-range: 0.3x
- Android Low-end: 0.15x
- Web Mobile: 0.2x
```

### Feature Availability Matrix

| Feature | iOS | Android | Web Desktop | Web Mobile |
|---------|-----|---------|-------------|------------|
| Camera | ✅ | ✅ | ✅* | ✅* |
| GPS | ✅ | ✅ | ⚠️ | ⚠️ |
| File Upload | ✅ | ✅ | ✅ | ✅ |
| Offline | ✅ | ✅ | ⚠️ | ⚠️ |
| Background Sync | ✅ | ⚠️ | ❌ | ❌ |

*Requires HTTPS
⚠️ Limited functionality
❌ Not available

### Memory Management Strategies

#### Mobile Platforms
- Regular garbage collection
- Limit active field count
- Cleanup on navigation
- Monitor memory usage
- Restart app if degraded

#### Desktop Platforms
- Less critical but monitor
- Browser tab memory limits
- Clear caches periodically
- Watch for memory leaks
- Profile with DevTools

## Platform Detection Patterns {important}

### User Agent Detection
```javascript
// Simplified platform detection
const iOS = /iPad|iPhone|iPod/.test(navigator.userAgent);
const Android = /Android/.test(navigator.userAgent);
const Mobile = /Mobile/.test(navigator.userAgent);
```

### Feature Detection
```javascript
// Preferred approach
const hasTouch = 'ontouchstart' in window;
const hasGPS = 'geolocation' in navigator;
const hasCamera = 'mediaDevices' in navigator;
```

## Platform-Specific Workarounds {comprehensive}

### iOS Workarounds
- HEIC conversion handling
- Safari IndexedDB limits
- Viewport keyboard issues
- Touch target sizing
- Memory limit monitoring

### Android Workarounds
- Storage permission flows
- Background service limits
- WebView version detection
- Manufacturer quirks
- Battery optimization

### Web Workarounds
- Polyfills for missing APIs
- Browser capability detection
- CORS handling
- Local storage fallbacks
- Print style sheets

## Testing Recommendations {essential}

### Minimum Test Devices
- iOS: iPhone SE (lowest spec)
- iOS: iPad (newest + 2 years old)
- Android: Low-end device (Go edition)
- Android: Flagship device
- Desktop: Chrome, Safari, Firefox

### Critical Test Scenarios
1. Memory pressure conditions
2. Slow network (3G simulation)
3. Permission denial flows
4. Background/foreground transitions
5. Orientation changes
6. Multi-tasking scenarios

## See Also {comprehensive}

### Field-Specific Platform Behaviors
- [Display Fields](../field-categories/display-field-v05.md#platform-behaviors)
- [Location Fields](../field-categories/location-fields-v05.md#platform-behaviors)
- [Media Fields](../field-categories/media-fields-v05.md#platform-behaviors)
- [Relationship Fields](../field-categories/relationship-field-v05.md#platform-behaviors)

### Related References
- [Performance Thresholds Reference](./performance-thresholds-reference.md)
- [Security Considerations Reference](./security-considerations-reference.md)
- [Troubleshooting Framework Reference](./troubleshooting-framework-reference.md)

## Metadata {comprehensive}
- **Document Version**: v01
- **Last Updated**: 2025-01-03
- **Status**: Initial extraction from field documentation
- **Purpose**: Consolidate platform-specific behaviors across all field types
- **Maintenance**: Update when new platform behaviors discovered