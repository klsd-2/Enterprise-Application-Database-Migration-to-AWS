# Database Migration Guide

## Steps:
1. Create AWS DMS instance
2. Configure source (on-prem DB)
3. Configure target (RDS)
4. Run full load migration
5. Enable CDC (Change Data Capture)

## Validation:
- Compare row counts
- Check data integrity
