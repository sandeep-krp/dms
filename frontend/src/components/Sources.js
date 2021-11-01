import React from 'react';
import axios from 'axios';
import {Table} from 'antd';
class Sources extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            sources: [],
            loading: true
        }
    }

    async getSourcesData() {
        try {
            const res = await axios.get('http://localhost:8080/api/v1/source')
            this.setState({ loading: false, sources: res.data })
        } catch {
            console.error("Could not get sources")
        }
    }

    componentDidMount() {
        this.getSourcesData()
    }

    render() {
        const columns = [
            {
                title: 'ID',
                key: 'id',
                dataIndex: 'id'
            },
            {
                title: 'Name',
                key: 'name',
                dataIndex: 'name'
            },
            {
                title: 'Schema',
                key: 'conf_blob',
                dataIndex: 'conf_blob',
                render: d => JSON.stringify(d)
            }
        ]
        return (<div style={{ height: 400, width: '70%' }}>
                <Table
                    dataSource = {this.state.sources}
                    columns = {columns}
                />
                </div>
        );
    }
}

export default Sources;