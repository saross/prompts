# Designer Limitations Reference
## Universal Constraints for All Fieldmark v3 Fields

### Overview

The Fieldmark Designer web application provides a visual interface for creating and configuring notebooks. While Designer handles most common configuration needs, certain advanced features and testing capabilities require direct JSON editing or can only be verified after deployment.

### Testing & Preview Limitations

#### Cannot Test Before Deployment
- **Field appearance**: No preview of how fields will render on different platforms
- **Conditional logic**: Conditions must be tested in deployed notebooks, not Designer preview
- **Validation behavior**: Cannot verify validation schemas work as intended
- **Mobile usability**: No way to test touch interactions or mobile-specific behaviors
- **Export formats**: Cannot preview CSV/JSON export behavior with sample data

#### Testing Workflow Impact
1. Make changes in Designer
2. Deploy to test server
3. Test on actual devices
4. Return to Designer for corrections
5. Repeat deployment cycle

This iterative process significantly impacts development time, especially for complex forms with conditional logic or platform-specific requirements.

### Validation Customization Constraints

#### Error Message Limitations
- **Cannot customize validation messages**: Stuck with Yup validation library defaults
  - Example: "This field is required" cannot be changed to "Please enter specimen ID"
  - Example: Email validation shows generic "Invalid email" rather than context-specific message
- **Cannot control error display positioning**: Errors always appear below fields
- **Cannot style error messages**: Red text styling is fixed
- **Cannot create contextual help**: Errors cannot reference other field values

#### Cross-Field Validation
Designer cannot create validation rules that reference multiple fields:
- Password confirmation matching
- Date range validation (start date before end date)
- Conditional required fields based on other field values
- Sum validation across numeric fields
- Duplicate checking across array fields

These require JSON editing with custom Yup schemas.

### Performance & Warning Gaps

#### No Performance Indicators
Designer provides no warnings when configurations will cause issues:
- **Option count limits**: No warning when Select/RadioGroup exceeds 20 options (causes lag with markdown processing)
- **Character limits**: No indication when text fields approach performance thresholds
- **Memory usage**: No warnings about large file uploads or image captures
- **Render complexity**: No indication when forms become too complex for mobile devices

#### Missing Accessibility Warnings
- No WCAG compliance indicators
- No color contrast warnings
- No touch target size validation (44×44px minimum)
- No screen reader compatibility checks
- No keyboard navigation testing

#### Platform-Specific Issues Not Flagged
- QRCodeFormField required on web (will block form submission)
- Address field initialization errors
- Browser-specific validation conflicts
- Mobile keyboard behavior issues

### Field Management Restrictions

#### Type Conversion Limitations
- **Cannot convert between field types**: Must delete and recreate
  - Example: Cannot change RadioGroup to Select
  - Example: Cannot convert TextField to MultipleTextField
  - Data migration must be handled externally

#### Bulk Operations Not Supported
- Cannot edit multiple fields simultaneously
- Cannot copy validation rules between fields
- Cannot apply consistent styling across field groups
- Cannot search and replace across field labels/helpers

#### Configuration Constraints
- **Character limits**: Cannot enforce maximum character counts
- **Input patterns**: Cannot restrict input format (phone numbers, postal codes)
- **Input masks**: Cannot create formatted input (credit cards, dates)
- **Auto-formatting**: Cannot enable automatic formatting as user types

### Advanced Features Requiring JSON

Despite Designer improvements, some features still require JSON editing:

#### Complex Hierarchies
While AdvancedSelect provides a JSON editor window, complex hierarchies still require careful manual construction:
- Multi-level taxonomies
- Conditional branches in hierarchies
- Large option trees (>100 nodes)

#### Component Parameters
Many component-specific parameters are not exposed in Designer:
- Platform-specific configurations
- Advanced Material-UI properties
- Custom CSS classes
- Performance optimizations

#### Meta Properties
While basic meta properties are available, advanced configurations require JSON:
- Custom annotation labels
- Conditional meta property display
- Meta property validation rules

### Workaround Strategies

#### For Testing Limitations
1. Maintain a staging deployment for rapid testing
2. Use device emulators for basic mobile testing
3. Create test notebooks with all field types
4. Document test cases for manual verification

#### For Validation Constraints
1. Use helper text to clarify requirements
2. Document validation rules in field labels
3. Create separate documentation for complex validation
4. Train users on expected formats

#### For Performance Issues
1. Monitor browser console during testing
2. Test with maximum expected data volumes
3. Document performance thresholds
4. Plan for progressive form complexity

### Impact on Development Workflow

These limitations affect different user groups:

**Notebook Designers**: Must plan for multiple deployment cycles and maintain external documentation for complex requirements.

**Developers**: Need to switch between Designer and JSON editing, maintaining synchronization between visual and code representations.

**End Users**: May encounter generic error messages and validation behaviors that don't match their domain expectations.

### Best Practices

1. **Start Simple**: Build basic structure in Designer, enhance with JSON
2. **Test Early**: Deploy frequently to catch issues before complex dependencies develop
3. **Document Thoroughly**: Maintain external documentation for validation rules and conditional logic
4. **Plan Iterations**: Budget time for the deploy-test-refine cycle
5. **Use Templates**: Create reusable patterns for common configurations

### Related Documentation
- Component Namespace Reference for JSON component names
- Validation Timing Reference for validation behavior
- Meta Properties Reference for annotation/uncertainty configuration
- Individual field documentation for field-specific limitations

### Version
Last updated: 2025-09-03
Applies to: Fieldmark v3 Designer (all versions)
Designer version: Current web interface