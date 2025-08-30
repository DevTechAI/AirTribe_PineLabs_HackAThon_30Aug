from flask import Blueprint, render_template
from app.models import Integration, db
from sqlalchemy import func

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
def dashboard():
    """Integration dashboard"""
    # Get integration statistics
    total_integrations = Integration.query.count()
    successful_integrations = Integration.query.filter_by(status='success').count()
    failed_integrations = Integration.query.filter_by(status='failed').count()
    
    # Get recent integrations
    recent_integrations = Integration.query.order_by(Integration.created_at.desc()).limit(10).all()
    
    # Get integration types breakdown
    type_stats = db.session.query(
        Integration.integration_type,
        func.count(Integration.id).label('count')
    ).group_by(Integration.integration_type).all()
    
    stats = {
        'total': total_integrations,
        'successful': successful_integrations,
        'failed': failed_integrations,
        'success_rate': (successful_integrations / total_integrations * 100) if total_integrations > 0 else 0,
        'type_breakdown': dict(type_stats)
    }
    
    return render_template('dashboard.html', 
                         stats=stats, 
                         recent_integrations=recent_integrations) 