# Accessibility Reference
## WCAG Compliance and Touch Target Standards for Fieldmark v3

### Overview

This document consolidates accessibility standards, WCAG compliance status, and touch target requirements for all Fieldmark v3 fields. Accessibility in fieldwork applications presents unique challenges: gloved hands, bright sunlight, muddy screens, and physical fatigue all impact usability. These guidelines address both standard WCAG compliance and field-specific accessibility needs.

### Touch Target Standards

#### Minimum Size Requirements

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

**CSS Override for Larger Targets**:
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
| **4.1.1** | Parsing | ✅ Pass | Valid HTML |
| **4.1.2** | Name, Role, Value | ⚠️ Partial | Some custom fields lack ARIA |

#### Level AA Compliance

| Criterion | Requirement | Fieldmark Status | Issues |
|-----------|-------------|------------------|--------|
| **1.3.5** | Identify Input Purpose | ✅ Pass | Semantic HTML used |
| **1.4.3** | Contrast (Minimum) | ⚠️ Partial | Some states below 4.5:1 |
| **1.4.4** | Resize Text | ✅ Pass | Text scalable to 200% |
| **1.4.5** | Images of Text | ✅ Pass | No text images used |
| **1.4.10** | Reflow | ⚠️ Partial | Some layouts break |
| **1.4.11** | Non-text Contrast | ❌ Fail | Spinner controls below 3:1 |
| **2.4.5** | Multiple Ways | N/A | Single page app |
| **2.4.6** | Headings and Labels | ✅ Pass | Descriptive labels |
| **2.4.7** | Focus Visible | ✅ Pass | Browser default focus |
| **2.5.5** | Target Size | ❌ Fail | Most fields below 44×44px |
| **3.3.3** | Error Suggestion | ⚠️ Partial | Generic error messages |
| **3.3.4** | Error Prevention | ⚠️ Partial | Limited validation |
| **4.1.3** | Status Messages | ❌ Fail | No aria-live regions |

### Field-Specific Accessibility Issues

#### Text Fields
- **Touch targets**: Default height ~36px (below 44px minimum)
- **Screen reader**: Labels announced properly
- **Keyboard**: Full navigation support
- **Issues**: Multiline text scrolling not announced

#### Number Fields
- **Spinners**: ~20×20px - far too small
- **Screen reader**: Type="number" provides semantic meaning
- **Keyboard**: Arrow keys adjust values
- **Issues**: No announcement of value changes via spinner

#### DateTime Fields
- **Native pickers**: Generally accessible
- **Platform variance**: Different interfaces confuse users
- **Screen reader**: Date format not always announced
- **Issues**: "Now" button location varies, may be missed

#### Selection Fields
- **Checkbox/Radio**: 24×24px icons too small
- **Labels not clickable**: Must hit exact icon
- **Screen reader**: Options announced
- **Issues**: Select and AdvancedSelect don't show error messages visually

#### Media Fields
- **Camera/QR**: Native UI generally accessible
- **Touch targets**: Full screen for capture
- **Issues**: Web platform shows disabled state without explanation

### Screen Reader Support

#### Tested Screen Readers
- **iOS**: VoiceOver
- **Android**: TalkBack
- **Windows**: NVDA, JAWS
- **macOS**: VoiceOver

#### Common Issues
1. **Error announcements**: Validation errors not always announced
2. **Dynamic content**: Field updates not announced
3. **Helper text**: Not consistently associated with fields
4. **State changes**: Touched/untouched state not conveyed
5. **Complex fields**: Address, AdvancedSelect structure not clear

#### ARIA Implementation Gaps
```html
<!-- Current (missing ARIA) -->
<input type="text" />

<!-- Needed for proper announcement -->
<input 
  type="text"
  aria-label="Field name"
  aria-describedby="helper-text error-message"
  aria-invalid="true"
  aria-required="true"
/>
<span id="helper-text">Helper text</span>
<span id="error-message" role="alert">Error message</span>
```

### Keyboard Navigation

#### Standard Keyboard Support
- **Tab**: Navigate between fields
- **Shift+Tab**: Navigate backwards
- **Enter**: Submit form or activate buttons
- **Space**: Toggle checkboxes, activate buttons
- **Arrow keys**: Navigate radio groups, adjust numbers
- **Escape**: Close dropdowns and pickers

#### Field-Specific Keyboard Behaviors
| Field Type | Keys | Action | Issues |
|------------|------|--------|--------|
| TextField | All keys | Standard typing | None |
| Number | ↑↓ | Increment/decrement | Step size not configurable |
| DateTime | Various | Platform-dependent | Inconsistent across browsers |
| Select | ↑↓ | Navigate options | Can't type to search |
| RadioGroup | ↑↓←→ | Navigate options | Must use arrows, not Tab |
| Checkbox | Space | Toggle | Enter key doesn't work |
| MultiSelect | ↑↓ Space | Select multiple | Complex interaction pattern |

### Color and Contrast

#### Current Contrast Ratios
| Element | Foreground | Background | Ratio | WCAG AA | WCAG AAA |
|---------|------------|------------|-------|---------|----------|
| Label text | #000000 | #FFFFFF | 21:1 | ✅ Pass | ✅ Pass |
| Input text | #000000 | #FFFFFF | 21:1 | ✅ Pass | ✅ Pass |
| Helper text | #666666 | #FFFFFF | 5.7:1 | ✅ Pass | ❌ Fail |
| Error text | #F44336 | #FFFFFF | 3.5:1 | ❌ Fail | ❌ Fail |
| Disabled | #9E9E9E | #FFFFFF | 2.8:1 | N/A | N/A |
| Focus ring | #1976D2 | #FFFFFF | 4.5:1 | ✅ Pass | ❌ Fail |

#### Color Blind Considerations
- Error states rely on red color (problematic for protanopia)
- Success states use green (problematic for deuteranopia)
- No patterns or icons to supplement color coding
- Recommendation: Add icons to validation states

### Platform-Specific Accessibility

#### iOS/iPadOS
- **VoiceOver**: Generally well-supported
- **Touch targets**: Many below 44×44pt minimum
- **Zoom**: Supported but may cause layout issues
- **Voice Control**: Limited support for custom fields

#### Android
- **TalkBack**: Good support for standard fields
- **Touch targets**: Below 48dp Material Design standard
- **Magnification**: Supported
- **Switch Access**: Not tested

#### Web Desktop
- **Screen readers**: Variable support
- **Keyboard**: Full support
- **High contrast mode**: Not optimized
- **Browser zoom**: Supported to 200%

### Field Operation Accessibility

Fieldwork presents unique accessibility challenges:

#### Environmental Factors
- **Bright sunlight**: Low contrast text hard to read
- **Rain/mud**: Precise touch targets impossible
- **Cold**: Reduced finger dexterity
- **Gloves**: Require larger touch targets
- **Fatigue**: Fine motor control degraded

#### Recommended Adaptations
1. **Increase all touch targets to 56×56px minimum**
2. **Use high contrast mode in bright conditions**
3. **Provide voice input alternatives**
4. **Minimize required precision interactions**
5. **Reduce scrolling requirements**
6. **Cache data aggressively for poor connectivity**

### Voice Input Support

#### Voice Dictation Compatibility
| Field Type | iOS Siri | Android | Dragon | Issues |
|------------|----------|----------|---------|--------|
| Text | ✅ Full | ✅ Full | ✅ Full | None |
| Number | ⚠️ Partial | ⚠️ Partial | ⚠️ Partial | Natural language not parsed |
| Email | ✅ Full | ✅ Full | ✅ Full | May need spelling |
| Date | ❌ Poor | ❌ Poor | ❌ Poor | Format not recognized |
| Selection | ❌ No | ❌ No | ❌ No | Can't select options |

#### Voice Command Support
- Currently no custom voice commands implemented
- Relies on platform-level voice control
- Limited interaction with custom components

### Testing Recommendations

#### Automated Testing
```javascript
// Using axe-core for automated accessibility testing
const axe = require('axe-core');

describe('Accessibility', () => {
  it('should have no violations', async () => {
    const results = await axe.run();
    expect(results.violations).toHaveLength(0);
  });
});
```

#### Manual Testing Checklist
- [ ] Test with screen reader on each platform
- [ ] Navigate using keyboard only
- [ ] Verify touch targets with measurement tool
- [ ] Test with platform zoom at 200%
- [ ] Verify color contrast ratios
- [ ] Test in high contrast mode
- [ ] Use with voice control
- [ ] Test with gloves/stylus
- [ ] Verify in bright sunlight
- [ ] Test with slow connection

#### User Testing
- Include users with disabilities in field trials
- Test with actual fieldwork conditions
- Document accessibility barriers encountered
- Prioritize fixes based on impact

### Compliance Roadmap

#### Priority 1: Critical (Safety/Legal)
1. Fix touch targets below 44×44px
2. Add aria-live regions for errors
3. Improve error message contrast
4. Fix label click areas

#### Priority 2: High (Usability)
1. Improve screen reader announcements
2. Add keyboard shortcuts
3. Enhance focus indicators
4. Implement skip navigation

#### Priority 3: Medium (Enhancement)
1. Add voice commands
2. Improve high contrast support
3. Create accessibility preferences
4. Add haptic feedback

### Implementation Guidelines

#### For Developers
1. Always include ARIA labels
2. Test with screen readers
3. Ensure 44×44px minimum touch targets
4. Provide keyboard alternatives
5. Use semantic HTML elements
6. Test contrast ratios
7. Include focus indicators

#### For Designers
1. Design for 56×56px touch targets in field
2. Don't rely solely on color
3. Provide clear visual hierarchy
4. Consider gloved hand interaction
5. Test in bright light conditions
6. Plan for offline/slow connectivity

#### For Project Managers
1. Budget for accessibility testing
2. Include users with disabilities in trials
3. Document accessibility requirements
4. Plan for progressive enhancement
5. Consider field conditions in requirements

### Known Limitations

#### Cannot Be Fixed
- Platform picker variations
- Native component accessibility bugs
- Third-party library limitations

#### Require Significant Rework
- Touch target sizes (CSS framework change)
- ARIA implementation (component rewrites)
- Screen reader support (architecture changes)

#### Workarounds Available
- Use external keyboard for precision
- Increase browser/OS zoom
- Use stylus for small targets
- Enable high contrast mode

### Resources

#### Testing Tools
- axe DevTools (browser extension)
- WAVE (WebAIM evaluation tool)
- Lighthouse (Chrome DevTools)
- Color contrast analyzers
- Screen reader testing guides

#### Standards Documentation
- WCAG 2.1 Guidelines
- iOS Human Interface Guidelines
- Material Design Accessibility
- ARIA Authoring Practices Guide

### Related Documentation
- Individual field documentation for specific issues
- Performance Thresholds Reference for interaction timing
- Designer Limitations Reference for configuration constraints
- Platform behavior documentation

### Version
Last updated: 2025-09-03
Applies to: Fieldmark v3 (all versions)
WCAG version: 2.1
Testing date: August 2025