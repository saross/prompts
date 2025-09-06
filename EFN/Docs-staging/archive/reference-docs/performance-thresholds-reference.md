# Performance Thresholds Reference

> **⚠️ DEPRECATED**: This document has been superseded by the consolidated [Platform Reference](../../references/platform-reference.md). This archived version is maintained for reference only.

## Empirically Tested Estimates for Fieldmark v3 Components

### Important Disclaimer

**These thresholds are ESTIMATES based on empirical observations, not guaranteed limits.** Performance varies significantly based on:
- Device specifications (CPU, RAM, storage)
- Browser type and version
- Network conditions
- Operating system
- Concurrent applications
- Data complexity

**Approach all thresholds with caution.** What works on a high-end device may fail on older hardware. Always test on your target devices under realistic conditions.

### We Welcome Your Feedback

These estimates are continuously refined based on user experiences. **Please share your observations:**
- If you encounter performance issues below these thresholds
- If you successfully exceed these thresholds
- Device-specific limitations you discover
- Optimization techniques that work for you

Contact the Fieldmark team or submit feedback through your project coordinator to help improve these guidelines.

### Overview

This document consolidates estimated performance thresholds and boundaries for Fieldmark v3 fields. These values are based on empirical testing across various devices and conditions. They should be used as conservative guidelines for notebook design, with actual limits varying based on deployment context.

### Testing Checklist

Use this checklist to verify your notebook stays within estimated performance boundaries:

- [ ] Forms have fewer than 50 fields per page
- [ ] Selection fields have fewer than 20 options (if using markdown)
- [ ] Text fields contain less than 10,000 characters
- [ ] No more than 10 validation rules per field
- [ ] Forms are paginated if exceeding thresholds
- [ ] Export datasets under 65,000 rows for Excel compatibility
- [ ] File uploads under 10MB per file
- [ ] Total form size under 100MB including attachments

## Field Count Thresholds (Estimates)

### Per Form/Page Limits

**Note:** These are conservative estimates. Your specific hardware may support more or fewer fields.

| Field Count | Performance Impact | User Experience | Recommendation |
|-------------|-------------------|-----------------|----------------|
| 1-20 fields | Optimal | Instant render (<500ms) | Ideal for mobile |
| 20-50 fields | Good | Fast render (<1s) | Acceptable for all platforms |
| 50-100 fields | Degraded | Noticeable delay (1-3s) | Consider pagination |
| 100-500 fields | Poor | Significant delay (3-10s) | Must paginate |
| 500-1000 fields | Critical | Very slow (10-30s) | Redesign required |
| >1000 fields | Failure | Browser crash likely | Not supported |

### Memory Consumption (Approximate)

**Note:** Memory usage varies by browser implementation and available system resources.

| Component Type | Memory Per Field | 100 Fields | 1000 Fields | Browser Limit |
|---------------|------------------|------------|-------------|---------------|
| Text fields | ~8KB | 800KB | 8MB | ~4GB typical |
| Number fields | ~8KB | 800KB | 8MB | ~4GB typical |
| Selection fields | ~12KB + options | 1.2MB+ | 12MB+ | Varies by options |
| Date fields | ~2MB (picker resources) | 200MB | 2GB | Critical at 100 fields |
| Media fields | ~5MB (camera access) | 500MB | 5GB | Critical at 20 fields |
| Map fields | ~10MB (map tiles) | 1GB | 10GB | Critical at 10 fields |

## Text Field Thresholds (Estimates)

### Character Limits

**Note:** These limits are approximations. Actual performance depends on character complexity and rendering requirements.

| Character Count | Field Type | Performance | Export Impact | Mobile Impact |
|----------------|------------|-------------|---------------|---------------|
| 0-50 | TextField | Optimal | None | Optimal |
| 50-500 | TextField/MultipleTextField | Optimal | None | Good |
| 500-1000 | MultipleTextField | Good | None | Good |
| 1000-5000 | MultipleTextField | Good | CSV may need escaping | Scrolling needed |
| 5000-10000 | MultipleTextField | Degraded | CSV reader issues possible | Performance lag |
| >10000 | MultipleTextField | Poor | Export problems likely | Severe lag |
| ~1MB | Any text field | Critical | CouchDB document limit | App crash |

### MultilineText Row Configuration

| Row Count | Use Case | Performance | Mobile Usability |
|-----------|----------|-------------|------------------|
| 3 rows | Brief notes | Optimal | Perfect |
| 4-5 rows | Standard descriptions | Optimal | Good |
| 6-8 rows | Detailed observations | Good | Requires scrolling |
| 10+ rows | Extended narratives | Good | Poor (excessive scrolling) |

## Selection Field Thresholds (Estimates)

### Option Count Limits

**Note:** Markdown processing adds variable overhead depending on markdown complexity.

| Option Count | Without Markdown | With Markdown | User Experience | Mobile Impact |
|-------------|------------------|---------------|-----------------|---------------|
| 1-5 options | Instant | Instant | Optimal | Perfect |
| 5-10 options | Instant | Fast (<100ms) | Optimal | Good |
| 10-20 options | Fast | Noticeable lag | Good | Scrolling needed |
| 20-50 options | Fast | Significant lag (>500ms) | Degraded | Poor scrolling |
| 50-100 options | Good | Poor (>1s) | Poor | Very poor |
| >100 options | Slow | Unusable | Redesign needed | Not viable |

**Note**: Markdown processing adds significant overhead. Consider disabling markdown for large option lists.

### AdvancedSelect Hierarchy Limits

| Node Count | Depth | Performance | Memory Usage | Recommendation |
|------------|-------|-------------|--------------|----------------|
| <50 nodes | 1-3 levels | Optimal | <1MB | Ideal |
| 50-100 nodes | 1-4 levels | Good | 1-2MB | Acceptable |
| 100-500 nodes | 2-5 levels | Degraded | 2-10MB | Consider alternatives |
| >500 nodes | Any | Poor | >10MB | Use search instead |

## Number Field Thresholds (Estimates)

### Validation Complexity

**Note:** Validation performance heavily depends on rule complexity, not just count.

| Validation Rules | Blur Response Time | User Experience | Recommendation |
|-----------------|-------------------|-----------------|----------------|
| 1-3 rules | <10ms | Instant | Optimal |
| 3-5 rules | 10-30ms | Fast | Good |
| 5-10 rules | 30-50ms | Noticeable | Acceptable |
| 10-15 rules | 50-200ms | Sluggish | Simplify if possible |
| >15 rules | >200ms | Poor | Must simplify |

### Numeric Precision Limits

| Value Range | Storage | Display | Excel Export | JavaScript Precision |
|------------|---------|---------|--------------|---------------------|
| -2^53 to 2^53 | Safe | Accurate | Accurate | Full precision |
| 15-17 digits | Safe | Accurate | Scientific notation | Full precision |
| >17 digits | Unsafe | Rounded | Loss of precision | Precision lost |
| Scientific notation | As string | Preserved | May convert | Preserved as string |

## DateTime Field Thresholds (Estimates)

### Form Limits

**Note:** Date picker resources vary significantly by platform and browser.

| Date Fields Per Form | Render Time | Memory Usage | Mobile Viability |
|---------------------|-------------|--------------|------------------|
| 1-10 fields | <500ms | 20MB | Excellent |
| 10-20 fields | 500ms-1s | 40MB | Good |
| 20-50 fields | 1-2s | 100MB | Degraded |
| 50-100 fields | 2-5s | 200MB | Poor |
| >100 fields | >5s | Browser limit | Not recommended |

### Processing Overhead

| Operation | Time Per Field | 100 Fields | Impact |
|-----------|---------------|------------|---------|
| Timezone conversion (DateTimeNow) | ~100ms | 10s | Significant for bulk operations |
| Picker rendering | 100-300ms | 10-30s | Affects initial load |
| Validation check | <5ms | 500ms | Minimal |
| Database indexing | ~500ms | 50s | One-time cost |

## Media Field Thresholds (Estimates)

### File Size Limits

**Note:** Upload times are highly dependent on network quality and server processing.

| File Size | Upload Time (3G) | Upload Time (WiFi) | Storage Impact | Recommendation |
|-----------|------------------|-------------------|----------------|----------------|
| <1MB | <5s | <1s | Minimal | Optimal |
| 1-5MB | 5-30s | 1-5s | Manageable | Good |
| 5-10MB | 30-60s | 5-10s | Significant | Maximum recommended |
| 10-50MB | 1-5min | 10-60s | Heavy | Requires warning |
| >50MB | >5min | >60s | Critical | Not recommended |

### Image Capture Specifications

| Resolution | File Size | Processing Time | Use Case |
|------------|-----------|-----------------|----------|
| 640x480 | ~200KB | <100ms | Thumbnails |
| 1280x720 (720p) | ~500KB | 200ms | Documentation |
| 1920x1080 (1080p) | ~1MB | 500ms | Standard quality |
| 3840x2160 (4K) | ~5MB | 2s | High quality |
| Original | Varies | Varies | Archival |

## Export Performance (Estimates)

### CSV Export Limits

**Note:** Export performance depends on data complexity, not just row count.

| Row Count | Generation Time | File Size | Excel Compatibility | Browser Handling |
|-----------|-----------------|-----------|-------------------|------------------|
| <1000 | <1s | <1MB | Perfect | Instant |
| 1000-10000 | 1-5s | 1-10MB | Good | Fast |
| 10000-65000 | 5-30s | 10-100MB | Last Excel limit | May timeout |
| 65000-100000 | 30-60s | 100MB+ | Requires splitting | Likely timeout |
| >100000 | >60s | >100MB | Database tools needed | Will timeout |

### JSON Export Performance

| Record Count | Generation Time | File Size | Memory Required | Recommendation |
|-------------|-----------------|-----------|-----------------|----------------|
| <100 | Instant | <100KB | Minimal | Optimal |
| 100-1000 | <2s | 100KB-1MB | <10MB | Good |
| 1000-10000 | 2-10s | 1-10MB | 10-100MB | Consider pagination |
| >10000 | >10s | >10MB | >100MB | Must paginate |

## Synchronization Thresholds (Estimates)

### Sync Payload Sizes

**Note:** Sync performance varies greatly with network latency and server load.

| Data Volume | Sync Time (3G) | Sync Time (WiFi) | Battery Impact | Recommendation |
|------------|----------------|------------------|----------------|----------------|
| <1MB | <10s | <2s | Minimal | Optimal |
| 1-10MB | 10-60s | 2-10s | Noticeable | Good |
| 10-50MB | 1-5min | 10-60s | Significant | Schedule for WiFi |
| 50-100MB | 5-10min | 1-5min | Heavy drain | WiFi only |
| >100MB | >10min | >5min | Critical | Requires chunking |

## Platform-Specific Thresholds (Estimates)

### Mobile Device Limits (iOS/Android)

**Note:** Mobile limits vary dramatically across device generations and manufacturers.

| Resource | Threshold | Impact | Mitigation |
|----------|-----------|---------|------------|
| RAM usage | >500MB | App termination risk | Reduce form complexity |
| Storage | >1GB | Sync issues | Implement cleanup |
| CPU usage | >80% for 30s | System throttling | Optimize operations |
| Battery drain | >10% per hour | User complaints | Reduce background ops |
| Network timeout | >30s | Connection drops | Implement retry logic |

### Browser-Specific Limits

| Browser | Memory Limit | Local Storage | IndexedDB | Session Storage |
|---------|-------------|---------------|-----------|-----------------|
| Chrome | 4GB typical | 10MB | 50% of disk | 10MB |
| Firefox | 2GB typical | 10MB | 50% of disk | 10MB |
| Safari | 2GB typical | 5MB | 1GB | 5MB |
| Edge | 4GB typical | 10MB | 50% of disk | 10MB |
| Mobile browsers | 512MB-1GB | 5-10MB | 50-500MB | 5MB |

## Performance Optimization Triggers

These estimated thresholds suggest when optimization should be considered:

### Must Optimize When:

1. **Form render time >3 seconds** → Implement pagination
2. **Field blur lag >50ms** → Simplify validation
3. **Option count >20 with markdown** → Disable markdown or reduce options
4. **Text field >10,000 characters** → Consider file attachment instead
5. **Memory usage >500MB mobile** → Reduce form complexity
6. **Export time >30 seconds** → Implement server-side export
7. **Sync payload >50MB** → Implement incremental sync

### Warning Thresholds:

1. **Form render 1-3 seconds** → Monitor and plan optimization
2. **Field blur lag 30-50ms** → Review validation complexity
3. **Option count 10-20** → Consider user experience
4. **Memory usage 200-500MB** → Begin optimization planning
5. **Export time 10-30 seconds** → Warn users about delay

## Testing Recommendations

**Remember:** These estimates are intentionally conservative. Your specific deployment may perform better or worse. Always conduct thorough testing on your actual target devices before deployment.

### Load Testing Scenarios

1. **Minimum viable test**: 10 fields, 5 records
2. **Standard test**: 50 fields, 100 records
3. **Stress test**: 100 fields, 1000 records
4. **Failure test**: 500 fields, 10000 records

### Device Testing Matrix

| Test Scenario | High-end Device | Mid-range Device | Low-end Device |
|--------------|-----------------|------------------|----------------|
| Small form (10 fields) | Must pass | Must pass | Must pass |
| Medium form (50 fields) | Must pass | Must pass | Should pass |
| Large form (100 fields) | Must pass | Should pass | May fail |
| Complex form (validation) | Must pass | Should pass | May fail |

### Network Testing Conditions

1. **WiFi**: Full functionality required
2. **4G/LTE**: Core functionality required
3. **3G**: Basic functionality required
4. **Offline**: Data entry must work
5. **Intermittent**: Graceful degradation required

## Best Practices

### Design Guidelines

1. **Prefer pagination**: Keep forms under 50 fields per page
2. **Simplify validation**: Maximum 5 rules per field
3. **Limit options**: Under 20 for selection fields
4. **Optimize media**: Compress images before upload
5. **Plan exports**: Implement pagination for large datasets

### Monitoring Metrics

Track these metrics in production:

1. Form render time (target: <1s)
2. Field validation time (target: <30ms)
3. Export generation time (target: <10s)
4. Sync completion rate (target: >95%)
5. Memory usage (target: <200MB mobile)
6. Battery drain (target: <5% per hour active use)

### Related Documentation

- Designer Limitations Reference for configuration constraints
- Data Export Reference for export-specific details
- Validation Timing Reference for validation performance
- Individual field documentation for field-specific thresholds

## Location Field Thresholds (Estimates)

### GPS Acquisition Times (TakePoint)

**Note:** GPS acquisition varies significantly based on environmental factors, satellite visibility, and device hardware.

| Platform | Cold Start | Warm Start | Indoor | Environmental Factors |
|----------|------------|------------|--------|----------------------|
| iOS | 3-8s | 1-3s | 15-30s | Best accuracy, A-GPS assisted |
| Android | 5-15s | 2-5s | 20-45s | Variable by device/manufacturer |
| Web | 2-5s | 1-2s | 10-20s | Browser-based, lower accuracy |

**Factors affecting acquisition:**
- Cold start: First GPS use after reboot or location services re-enabled
- Warm start: GPS used within last hour
- Indoor: Significant signal degradation through buildings
- Urban canyon: Tall buildings create multipath interference

### Map Performance (MapFormField)

**Note:** Performance degrades exponentially with vertex count. Mobile devices particularly affected.

| Vertices | Desktop | iOS | Android | Performance Impact |
|----------|---------|-----|---------|-------------------|
| <100 | Instant | Instant | Instant | Optimal - recommended for all platforms |
| 100-300 | <100ms | <200ms | <300ms | Good - acceptable for most uses |
| 300-500 | <200ms | <400ms | <600ms | Acceptable - noticeable on older devices |
| 500-1000 | <500ms | <1s | 1-2s | Poor - significant lag, avoid on mobile |
| 1000-2000 | 1-2s | 2-4s | 4-8s | Critical - high crash risk |
| >2000 | 2-5s | Crash risk | Crash likely | Not supported |

**Additional constraints:**
- GPU acceleration disabled for compatibility
- No WebGL fallback implemented
- Memory not released between edits

### Battery Consumption (Location Features)

**Note:** Battery drain estimates based on typical usage patterns. Actual consumption varies by device age and battery health.

| Operation | Battery/Hour | Continuous Use | Notes |
|-----------|--------------|----------------|-------|
| TakePoint (high accuracy) | 8-12% | Not recommended | GPS constantly active |
| TakePoint (balanced) | 4-6% | Acceptable | Standard accuracy mode |
| MapFormField (active drawing) | 2-3% | Sustainable | CPU for rendering only |
| MapFormField (map visible) | <1% | Negligible | Static map display |
| Combined usage | 10-15% | Limited time | Both features active |

**Battery optimization tips:**
- Space TakePoint captures at least 60 seconds apart
- Use `enableHighAccuracy: false` when 10-15m accuracy acceptable
- Close map view when not actively drawing
- Consider external battery pack for all-day fieldwork

### Storage Requirements (Offline Maps)

| Coverage Area | Zoom Levels | Approximate Size | Download Time (4G) |
|--------------|-------------|------------------|-------------------|
| City district (25 km²) | 10-18 | 50-100 MB | 1-2 minutes |
| Survey area (100 km²) | 12-19 | 100-200 MB | 2-4 minutes |
| Regional (1000 km²) | 8-16 | 200-500 MB | 5-10 minutes |
| Country subset | 6-14 | 500MB-1GB | 10-20 minutes |

**Storage considerations:**
- Browser storage typically limited to 50% of free disk space
- Mobile apps may have lower limits (varies by OS)
- Tile cache persists until explicitly cleared
- Consider selective download of work areas only

### Location Data Limits

| Metric | TakePoint | MapFormField | Impact |
|--------|-----------|--------------|---------|
| Points per notebook | 1000-2000 | N/A | Performance degrades beyond |
| Vertices per feature | N/A | 500 optimal, 2000 max | Drawing responsiveness |
| Coordinate precision | 14+ decimals shown | User-controlled | False precision displayed |
| GPS timeout | 10s default, 45s max | N/A | Acquisition wait time |
| Accuracy display | Always shown | Not captured | Metres to 1 decimal |

### Version
Last updated: 2025-09-04
Applies to: Fieldmark v3 (all versions)
Performance metrics: Empirically estimated August 2025
Location metrics: Added January 2025

### Feedback and Contributions

These thresholds are living estimates that improve with community input. Please report your experiences to help refine these guidelines for future users. Remember: your mileage may vary - always test on your actual deployment hardware.