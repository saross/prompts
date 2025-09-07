<!-- concat:boundary:start section="platform-reference" -->
<!-- concat:metadata
document_id: platform-reference
category: references
version: 1.0
last_updated: 2025-01-06
purpose: Comprehensive technical reference for platform behaviors, performance thresholds, accessibility, and troubleshooting
source_documents:
  - platform-behaviors-reference.md (9KB)
  - performance-thresholds-reference.md (18KB)
  - accessibility-reference.md (13KB)
  - troubleshooting-framework-reference.md (9KB) - platform issues only
-->

<!-- discovery:metadata
provides: [platform-behaviors, mobile-issues, browser-differences, offline-support]
see-also: [location-fields, media-fields, constraints-reference]
-->


# Platform Reference

## Overview {essential}

This comprehensive reference consolidates all platform-specific technical details for Fieldmark v3, including behaviors across iOS, Android, Web Desktop, and Web Mobile platforms, performance thresholds, accessibility standards, and platform-specific troubleshooting. All performance thresholds are estimates based on empirical observations and code analysis - they are advisory only and should be tested with your specific hardware and use cases. We welcome performance feedback to improve these estimates.

## Platform Characteristics Summary {essential}

| Platform | Performance | UI Framework | Primary Constraints |
|----------|-------------|--------------|-------------------|
| iOS | Moderate | Native WebView | Memory limits, permission cascades |
| Android | Variable | Chrome WebView | Device fragmentation, background restrictions |
| Web Desktop | Fast | Browser native | Full offline support via PouchDB |
| Web Mobile | Slow | Mobile browser | Limited memory, touch UI, offline via PouchDB |

### Relative Performance Scaling

**Note**: These are approximate performance ratios based on empirical testing and code analysis. They are advisory estimates only - actual performance varies significantly by device. We welcome performance feedback to refine these estimates.

```
Relative Performance (normalized to Web Desktop = 1.0):
- Web Desktop: 1.0x (baseline)
- iOS Native: 0.5x
- Android High-end: 0.6x
- Android Mid-range: 0.3x
- Android Low-end: 0.15x
- Web Mobile: 0.2x
```

## iOS Platform Behaviors {important}

### System Characteristics
- **Rendering Engine**: WebKit/Safari
- **Memory Limit**: ~200MB before crash (approximate)
- **JavaScript Execution**: Single-threaded with 10s timeout
- **Local Storage**: 50MB IndexedDB limit
- **Performance**: ~2x slower than native apps (estimated)

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

### iOS-Specific Workarounds
- HEIC conversion handling
- Safari IndexedDB limits
- Viewport keyboard issues
- Touch target sizing
- Memory limit monitoring

## Android Platform Behaviors {important}

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

### Android-Specific Workarounds
- Storage permission flows
- Background service limits
- WebView version detection
- Manufacturer quirks
- Battery optimization

## Web Desktop Platform {important}

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

### Capabilities & Limitations
- **Offline Support**: Full offline capability via PouchDB (same as mobile)
- **Sync**: Opportunistic sync when network available
- **Fallback Option**: Users often use web on tablets/laptops when app fails
- No native GPS (IP/WiFi geolocation only)
- No camera access without HTTPS
- Local storage varies by browser
- Print formatting inconsistent

## Web Mobile Platform {important}

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

## Performance Thresholds {important}

### Important Disclaimer

**These thresholds are ESTIMATES based on empirical observations and code analysis - they are advisory only, not guaranteed limits.** Performance varies significantly based on:
- Device specifications (CPU, RAM, storage)
- Browser type and version
- Network conditions
- Operating system
- Concurrent applications
- Data complexity

**Always test on your target devices under realistic conditions.**

### Field Count Thresholds (Estimates)

#### Per Form/Page Limits

**Note**: These are conservative estimates extrapolated from code analysis and testing. Your specific hardware may support more or fewer fields. We welcome performance feedback to improve these advisory thresholds.

| Field Count | Performance Impact | User Experience | Recommendation |
|-------------|-------------------|-----------------|----------------|
| 1-20 | Minimal | Smooth | Ideal for all platforms |
| 21-50 | Noticeable on low-end | Good | Acceptable for most cases |
| 51-100 | Significant on mobile | Degraded | Split forms recommended |
| 100+ | Severe on all platforms | Poor | Must split into pages |

#### Memory Consumption (Approximate)

| Field Type | Memory per Field | 50 Fields | 100 Fields |
|------------|-----------------|-----------|------------|
| Text | ~5KB | 250KB | 500KB |
| Number | ~3KB | 150KB | 300KB |
| Selection | ~10KB | 500KB | 1MB |
| DateTime | ~8KB | 400KB | 800KB |
| Location | ~20KB | 1MB | 2MB |
| Photo | ~50KB + image | 2.5MB+ | 5MB+ |
| Relationship | ~15KB | 750KB | 1.5MB |

### Text Field Thresholds {#text-field-performance}

#### Character Limits

| Character Count | Performance | Mobile Impact | Desktop Impact |
|-----------------|-------------|---------------|----------------|
| < 1,000 | Excellent | None | None |
| 1,000-5,000 | Good | Minimal | None |
| 5,000-10,000 | Acceptable | Typing lag | None |
| 10,000-50,000 | Poor | Severe lag | Noticeable |
| > 50,000 | Unusable | App crash likely | Browser hang |

### Selection Field Thresholds {#selection-performance}

#### Option Count Limits

| Options | RadioGroup | Select | MultiSelect | AdvancedSelect |
|---------|------------|--------|-------------|----------------|
| 1-5 | Excellent | Excellent | Excellent | Overkill |
| 6-20 | Good | Excellent | Good | Good |
| 21-50 | Poor (use Select) | Good | Acceptable | Excellent |
| 51-100 | N/A | Acceptable | Poor | Good |
| 100-500 | N/A | Poor | Very Poor | Acceptable |
| 500+ | N/A | Unusable | Unusable | Poor |

### Media Field Thresholds {#media-performance}

#### File Size Limits

| File Size | Upload Time (4G) | Upload Time (3G) | Mobile Impact |
|-----------|------------------|------------------|---------------|
| < 1MB | < 2 sec | < 10 sec | Minimal |
| 1-5MB | 2-10 sec | 10-50 sec | Noticeable |
| 5-10MB | 10-20 sec | 50-100 sec | Significant |
| 10-25MB | 20-50 sec | 100-250 sec | App may crash |
| > 25MB | > 50 sec | > 250 sec | Likely to fail |

#### Image Specifications

| Resolution | File Size (JPG) | Processing Time | Battery Impact |
|------------|-----------------|-----------------|----------------|
| 640×480 | ~100KB | < 1 sec | Minimal |
| 1920×1080 | ~500KB | 1-2 sec | Low |
| 3024×4032 | ~2MB | 3-5 sec | Medium |
| 4032×3024 | ~3MB | 5-10 sec | High |
| Original | Varies | 10+ sec | Very High |

### Export Performance {#export-performance}

#### CSV Export Limits

| Rows | Columns | Export Time | File Size | Excel Compatible |
|------|---------|-------------|-----------|------------------|
| < 1,000 | < 50 | < 1 sec | < 1MB | Yes |
| 1,000-10,000 | < 100 | 1-5 sec | 1-10MB | Yes |
| 10,000-65,000 | < 200 | 5-30 sec | 10-50MB | Yes |
| 65,000-100,000 | Any | 30-60 sec | 50-100MB | No (Excel limit) |
| > 100,000 | Any | > 60 sec | > 100MB | No |

## Accessibility Standards {comprehensive}

### Touch Target Requirements

#### Minimum Size Standards

| Standard | Minimum Size | Applies To | Fieldmark Status |
|----------|-------------|------------|------------------|
| **WCAG 2.1 (2.5.5)** | 44×44 CSS pixels | All interactive elements | ⚠️ Partial compliance |
| **iOS HIG** | 44×44 points | All touch targets | ❌ Many fields below minimum |
| **Material Design** | 48×48 dp | All touch targets | ❌ Most fields below minimum |
| **Field Best Practice** | 56×56 pixels | Primary actions in field | ❌ Not met by default |

#### Current Touch Target Sizes

| Field Type | Default Size | Compliant? | Issue |
|------------|--------------|------------|-------|
| **TextField** | ~36px height | ❌ No | Below all standards |
| **Number spinners** | ~20×20px | ❌ No | Far too small for field use |
| **Checkbox** | 24×24px | ❌ No | Icon only, label not clickable |
| **Radio buttons** | 24×24px | ❌ No | Small target, label not clickable |
| **Select dropdown** | ~36px height | ❌ No | Below minimum |
| **Date pickers** | Platform varies | ✅ Usually | Native pickers generally compliant |
| **Camera button** | Platform varies | ✅ Yes | Native camera UI compliant |
| **QR scanner** | Full screen | ✅ Yes | Entire screen is target |

#### Touch Target Solutions

```css
/* Minimum WCAG compliance */
.MuiInputBase-root {
  min-height: 44px !important;
}

/* Field-optimized (gloves, fatigue) */
.MuiInputBase-root {
  min-height: 56px !important;
  font-size: 16px !important; /* Prevents zoom on iOS */
}

/* Number field spinners */
.MuiInputBase-root input[type="number"]::-webkit-inner-spin-button,
.MuiInputBase-root input[type="number"]::-webkit-outer-spin-button {
  height: 44px;
  width: 44px;
}
```

### WCAG 2.1 Compliance Status

**Note**: Improved adherence to accessibility standards is on our roadmap but not fully implemented. Current status reflects known gaps that are being addressed.

#### Level A Compliance

| Criterion | Requirement | Fieldmark Status | Issues |
|-----------|-------------|------------------|--------|
| **1.1.1** | Non-text Content | ✅ Pass | Icons have labels |
| **1.3.1** | Info and Relationships | ⚠️ Partial | Some fields lack proper ARIA |
| **1.4.1** | Use of Color | ✅ Pass | Not solely color-dependent |
| **2.1.1** | Keyboard | ✅ Pass | All fields keyboard accessible |
| **2.4.3** | Focus Order | ✅ Pass | Logical tab order |
| **3.1.1** | Language of Page | ✅ Pass | HTML lang attribute set |
| **3.3.1** | Error Identification | ⚠️ Partial | Some fields don't show errors |
| **3.3.2** | Labels or Instructions | ✅ Pass | All fields have labels |

#### Level AA Compliance

| Criterion | Requirement | Fieldmark Status | Issues |
|-----------|-------------|------------------|--------|
| **1.4.3** | Contrast (Minimum) | ⚠️ Partial | Some states below 4.5:1 |
| **1.4.11** | Non-text Contrast | ❌ Fail | Spinner controls below 3:1 |
| **2.5.5** | Target Size | ❌ Fail | Most fields below 44×44px |
| **3.3.3** | Error Suggestion | ⚠️ Partial | Generic error messages |
| **4.1.3** | Status Messages | ❌ Fail | No aria-live regions |

### Field-Specific Accessibility Issues

#### Text Fields {#text-field-accessibility}
- **Touch targets**: Default height ~36px (below 44px minimum)
- **Screen reader**: Labels announced properly
- **Keyboard**: Full navigation support
- **Issues**: Multiline text scrolling not announced

#### Number Fields {#number-field-accessibility}
- **Spinners**: ~20×20px - far too small
- **Screen reader**: Type="number" provides semantic meaning
- **Keyboard**: Arrow keys for increment/decrement
- **Issues**: Spinner controls not keyboard accessible

#### Selection Fields {#selection-field-accessibility}
- **Checkbox/Radio**: 24×24px targets too small
- **Screen reader**: Options announced
- **Keyboard**: Space to select, arrows to navigate
- **Issues**: Label text not clickable

#### DateTime Fields {#datetime-field-accessibility}
- **Touch targets**: Native pickers usually compliant
- **Screen reader**: Date announced in locale format
- **Keyboard**: Complex navigation varies by platform
- **Issues**: Custom pickers may not be accessible

#### Media Fields {#media-field-accessibility}
- **Camera button**: Platform native (usually compliant)
- **File upload**: Browser native (compliant)
- **Screen reader**: Upload status not announced
- **Issues**: No progress indicators for screen readers

#### Location Fields {#location-field-accessibility}
- **GPS button**: Varies by implementation
- **Map**: Often not keyboard navigable
- **Screen reader**: Coordinates not announced
- **Issues**: Map interactions not accessible

### Contrast Requirements

#### Text Contrast
- Normal text: 4.5:1 minimum
- Large text (18pt+): 3:1 minimum
- Fieldmark status: ⚠️ Some states fail

#### UI Component Contrast
- Interactive components: 3:1 minimum
- Focus indicators: 3:1 minimum
- Fieldmark status: ❌ Many components fail

### Field-Specific Recommendations

1. **Increase all touch targets** to minimum 44×44px
2. **Add ARIA labels** to custom components
3. **Implement aria-live** for dynamic updates
4. **Increase contrast** for error states
5. **Make labels clickable** for checkboxes/radios
6. **Add keyboard shortcuts** for common actions
7. **Provide skip links** for long forms
8. **Test with screen readers** on all platforms

## Platform-Specific Troubleshooting {comprehensive}

### Diagnostic Framework

1. **Identify Symptoms** - What exactly is occurring?
2. **Check Console** - Browser/app console for errors
3. **Verify Platform** - iOS, Android, or Web-specific?
4. **Test Isolation** - Minimal test case?
5. **Check Configuration** - Valid JSON?
6. **Review Logs** - Sync, network, validation
7. **Document Pattern** - Reproducible steps

### Platform Detection Patterns

#### User Agent Detection
```javascript
// Simplified platform detection
const iOS = /iPad|iPhone|iPod/.test(navigator.userAgent);
const Android = /Android/.test(navigator.userAgent);
const Mobile = /Mobile/.test(navigator.userAgent);
```

#### Feature Detection (Preferred)
```javascript
const hasTouch = 'ontouchstart' in window;
const hasGPS = 'geolocation' in navigator;
const hasCamera = 'mediaDevices' in navigator;
```

### iOS Debugging

#### Safari Web Inspector
```javascript
// Enable in Settings → Safari → Advanced → Web Inspector
console.log('iOS state:', navigator.userAgent);
// Check memory
performance.memory
```

#### Common iOS Issues
- Memory crashes at ~200MB
- HEIC conversion failures
- Permission cascade problems
- IndexedDB quota exceeded
- Viewport keyboard overlap

### Android Debugging

#### Chrome DevTools
```bash
# Enable USB debugging
# Navigate to chrome://inspect
adb logcat | grep Fieldmark
```

#### Common Android Issues
- WebView version incompatibility
- Storage permission complexity
- Background service killing
- Manufacturer customizations
- Battery optimization interference

### Web Desktop Debugging

#### Browser DevTools
```javascript
debugger; // Breakpoint
console.time('Operation');
// ... operation
console.timeEnd('Operation');
```

#### Common Desktop Issues
- CORS restrictions
- Local storage limits
- Browser extension conflicts
- Mixed content blocking
- Cache invalidation

### Performance Optimization Triggers

#### Must Optimize When:
- Form load time > 3 seconds
- Typing lag > 100ms
- Save operation > 5 seconds
- Memory usage > 100MB mobile
- Battery drain > 20% per hour

#### Warning Thresholds:
- 30+ fields visible simultaneously
- 50+ options in selection field
- 10+ photos per record
- 5+ concurrent API calls
- 3+ levels of nested conditions

### Platform-Specific Error Messages

| Error | Platform | Cause | Fix |
|-------|----------|-------|-----|
| `QuotaExceededError` | iOS Safari | IndexedDB full | Clear app data |
| `Permission denied` | iOS/Android | Missing permission | Settings → App |
| `Network timeout` | All | Slow connection | Retry/offline mode |
| `Out of memory` | Mobile | Too many fields | Reduce form size |
| `WebView crashed` | Android | Memory/compatibility | Update WebView |

## Feature Availability Matrix {comprehensive}

| Feature | iOS | Android | Web Desktop | Web Mobile |
|---------|-----|---------|-------------|------------|
| Camera | ✅ | ✅ | ✅* | ✅* |
| GPS | ✅ | ✅ | ⚠️ | ⚠️ |
| File Upload | ✅ | ✅ | ✅ | ✅ |
| Offline | ✅ | ✅ | ⚠️ | ⚠️ |
| Background Sync | ✅ | ⚠️ | ❌ | ❌ |
| QR Scanning | ✅ | ✅ | ❌ | ❌ |
| Push Notifications | ✅ | ✅ | ⚠️ | ❌ |
| Biometric Auth | ✅ | ✅ | ❌ | ❌ |

*Requires HTTPS  
⚠️ Limited functionality  
❌ Not available  

## Testing Recommendations {comprehensive}

### Minimum Test Devices
- **iOS**: iPhone SE (lowest spec)
- **iOS**: iPad (newest + 2 years old)
- **Android**: Low-end device (Go edition)
- **Android**: Flagship device
- **Desktop**: Chrome, Safari, Firefox

### Critical Test Scenarios
1. Memory pressure conditions
2. Slow network (3G simulation)
3. Permission denial flows
4. Background/foreground transitions
5. Orientation changes
6. Multi-tasking scenarios
7. Battery drain monitoring
8. Offline/online transitions

### Load Testing Scenarios
1. Maximum fields per form
2. Maximum options per select
3. Maximum photos per record
4. Maximum concurrent users
5. Maximum export size
6. Maximum sync payload

### Network Testing Conditions
- **Fast 4G**: Baseline performance
- **Slow 3G**: Common field condition
- **Offline**: Required capability
- **Intermittent**: Reality in remote areas
- **High latency**: Satellite connections

## Best Practices Summary {comprehensive}

### Design Guidelines

#### DO:
✅ Test on minimum spec devices  
✅ Design for 3G networks  
✅ Keep forms under 50 fields  
✅ Implement platform detection  
✅ Provide offline capability  
✅ Use native UI components  
✅ Monitor memory usage  
✅ Implement proper permissions flow  

#### DON'T:
❌ Assume high-end devices  
❌ Require constant connectivity  
❌ Create forms with 100+ fields  
❌ Ignore platform differences  
❌ Use tiny touch targets  
❌ Skip accessibility testing  
❌ Ignore battery impact  
❌ Bypass native controls  

### Performance Optimization

1. **Split large forms** into multiple pages
2. **Lazy load** images and heavy content
3. **Debounce** validation and search
4. **Cache** frequently accessed data
5. **Compress** images before upload
6. **Minimize** real-time calculations
7. **Paginate** large datasets
8. **Optimize** for mobile first

### Accessibility Priorities

1. **Increase touch targets** to 44×44px minimum
2. **Ensure keyboard navigation** for all features
3. **Add ARIA labels** for screen readers
4. **Maintain color contrast** ratios
5. **Provide text alternatives** for images
6. **Support browser zoom** to 200%
7. **Test with assistive technology**
8. **Document accessibility features**

## Monitoring Metrics {comprehensive}

### Performance Metrics
- Form load time (target: <3s)
- Input latency (target: <100ms)
- Save time (target: <5s)
- Export time (target: <30s)
- Memory usage (target: <100MB mobile)
- Battery drain (target: <20%/hour)

### User Experience Metrics
- Touch target compliance
- Error recovery success rate
- Offline capability usage
- Permission grant rate
- Form completion rate
- Platform-specific crash rate

## Migration Considerations {comprehensive}

### Platform Migration Paths
- **Native → PWA**: Gradual feature parity
- **Desktop → Mobile**: Responsive design required
- **Online → Offline**: Sync architecture needed
- **Single → Multi-platform**: Abstract platform APIs

### Version Compatibility
- Minimum iOS: 12.0
- Minimum Android: 7.0 (API 24)
- Minimum Chrome: 80
- Minimum Safari: 12
- Minimum Firefox: 78

## Related Documentation {important}

- [Component Reference](./component-reference.md) - Component technical details
- [Operations Reference](./operations-reference.md) - Operational procedures
- [Constraints Reference](./constraints-reference.md) - System limitations
- [Implementation Patterns Guide](../patterns/implementation-patterns-guide.md) - Common patterns
- Individual field documentation for field-specific platform behaviors

## Version Information {comprehensive}

- **Last Updated**: 2025-01-06
- **Applies to**: Fieldmark v3 (all versions)
- **Platform Coverage**: iOS, Android, Web Desktop, Web Mobile
- **Performance Data**: Based on empirical testing
- **Accessibility Standards**: WCAG 2.1 Level AA target

**Important**: All performance thresholds are estimates based on code analysis and empirical testing - they are advisory only. Always test with your actual devices and data. We welcome performance feedback to refine these estimates.

<!-- concat:boundary:end section="platform-reference" -->