# PropCast Property Comparison Feature

## Overview
The Property Comparison feature allows users to select and compare two properties side-by-side with detailed analysis and interactive Plotly visualizations.

## Features

### 1. **Property Selection Page** (`/properties/`)
- Clean, intuitive UI with two columns
- Left column: Select Property 1
- Right column: Select Property 2
- Click any property card to select it
- Selected properties highlight in green
- Status indicators show which properties are selected
- "Compare Selected Properties" button enables only when two different properties are selected

### 2. **Comparison View** (`/compare/`)
- **Side-by-Side Property Cards**
  - Property 1 (Red border): Shows all details
  - Property 2 (Green border): Shows all details
  - Color-coded badges for easy identification
  
- **Detailed Property Information**
  - Location
  - BHK Type
  - Area (sq ft)
  - Price (Lakhs)
  - Price per square foot
  - Status (Sold/Available)
  - Property Age (Years)
  - Parking availability

### 3. **Interactive Plotly Chart**
- **Price vs Area Scatter Plot**
  - Blue dots: All properties in the dataset
  - Red star: Property 1 (highlighted)
  - Green diamond: Property 2 (highlighted)
  - Hover information shows property details
  - Responsive and fully interactive
  - Legend showing what each marker represents

## How to Use

### Step 1: Upload Property Data
1. Go to the home page (`/`)
2. Upload a CSV file with columns: `Location`, `BHK`, `Area_sqft`, `Price_Lakhs`, `Age_Years`, `Parking`, `Status`
3. Verify data is loaded

### Step 2: Navigate to Comparison
1. Click **⚖️ Compare Properties** button in the navbar
2. You'll see the property selection page with all available properties

### Step 3: Select Properties
1. **Select Property 1**: Click on any property card in the left column
   - The card will highlight in green
   - Status shows "Property 1: [Location Name]"
2. **Select Property 2**: Click on any different property card in the right column
   - The card will highlight in green
   - Status shows "Property 2: [Location Name]"

### Step 4: View Comparison
1. Once two different properties are selected, the **"⚖️ Compare Selected Properties"** button becomes active
2. Click it to go to the comparison view
3. View detailed side-by-side comparison cards
4. Analyze the Plotly chart showing price vs area for all properties
5. Use back button to select different properties

## CSV Format

Your upload CSV must have these columns:

```
Location, BHK, Area_sqft, Price_Lakhs, Age_Years, Parking, Status
```

Example:
```
Gachibowli - Hyderabad,2,1200,85,3,Yes,Sold
Kondapur - Hyderabad,3,1800,145,7,Yes,Available
```

## Features & Benefits

### Visual Design
- ✅ Consistent Bootstrap 5 styling
- ✅ Responsive on mobile and desktop
- ✅ Color-coded properties (Red for Property 1, Green for Property 2)
- ✅ Clear visual hierarchy

### Functionality
- ✅ Click-based property selection (no radio buttons)
- ✅ Real-time status updates
- ✅ Price per sqft calculation
- ✅ Interactive Plotly scatter chart with markers
- ✅ Comprehensive error handling
- ✅ Session persistence for CSV data

### User Experience
- ✅ Intuitive two-column layout
- ✅ Clear navigation with back buttons
- ✅ Visual feedback on selections
- ✅ Descriptive error messages
- ✅ Mobile-responsive design

## Technical Details

### Views Used
- `properties_list()` - Property selection interface
- `compare_properties()` - Comparison and chart generation

### Routes
- `/properties/` - Property selection page
- `/compare/?prop1=INDEX&prop2=INDEX` - Comparison view

### Files Modified
- `core/views.py` - Added comparison functions
- `core/urls.py` - Added comparison routes
- `templates/properties_list.html` - Property selection UI
- `templates/compare.html` - Comparison display
- `templates/upload.html` - Updated navbar
- `templates/predict.html` - Updated navbar

### Chart Library
- **Plotly Express** for interactive visualizations
- Scatter plot with custom markers and highlighting
- Responsive height and responsive resizing

## Troubleshooting

### CSV Not Found Error
- Ensure CSV is uploaded on the home page first
- Check media folder exists at `PROJECT_ROOT/media/`

### Properties Not Showing
- Verify CSV has required columns: `Location`, `Area_sqft`, `Price_Lakhs`
- Check CSV is valid (no encoding issues)

### Chart Not Rendering
- Ensure Plotly.js is loaded (check browser console)
- Verify `Area_sqft` and `Price_Lakhs` columns contain numeric values

### Selection Button Disabled
- Make sure two **different** properties are selected
- Cannot compare a property with itself

## Future Enhancements

Potential improvements:
- Export comparison as PDF report
- Add more chart types (bar charts, distribution plots)
- Property filters by location, price range, BHK
- Save favorite comparisons
- Email comparison results
- Advanced analytics (ROI, depreciation trends)

---

**Version**: 1.0  
**Last Updated**: 2026-06-06
